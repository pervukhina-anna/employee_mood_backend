from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import Department, Hobby, Position, User

from .fields import Base64ImageField


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = ('id', 'name', 'chief_position')


class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    department = DepartmentSerializer(read_only=True)
    position = PositionSerializer(read_only=True)
    hobbies = HobbySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'patronymic', 'role',
            'department', 'position', 'hobbies', 'avatar', 'about', 'phone',
            'date_joined'
        )


class UserSelfUpdateSerializer(serializers.ModelSerializer):
    '''Для редактирования своего профиля'''

    avatar = Base64ImageField()
    hobbies = HobbySerializer

    class Meta:
        model = User
        fields = ('about', 'avatar', 'hobbies')


class UserUpdateSerializer(serializers.ModelSerializer):
    '''Для редактирования профилей сотрудников HR'ом'''

    department = DepartmentSerializer
    position = PositionSerializer
    role = serializers.ChoiceField(choices=['employee', 'chief'])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic',
                  'department', 'position', 'role', 'phone')

    def validate(self, data):
        if self.instance and self.instance.is_hr:
            raise serializers.ValidationError(
                'Нельзя редактировать сотрудника с ролью HR.'
            )
        return data

    def validate_position(self, value):
        department = self.initial_data.get('department')
        position = self.initial_data.get('position')

        if position is None:
            return value

        if department:
            if not value.departments.filter(pk=department).exists():
                raise serializers.ValidationError(
                    'Выбранная должность не относится к указанному отделу.'
                )

        user_department = self.instance.department

        if user_department:
            if not value.departments.filter(pk=user_department.pk).exists():
                raise serializers.ValidationError(
                    'Выбранная должность не относится к текущему отделу '
                    'пользователя.'
                )
        else:
            self.initial_data.pop('position')

        return value

    def validate_department(self, value):
        department = self.initial_data.get('department')
        position = self.initial_data.get('position')

        if department is None and position:
            self.initial_data.pop('position', None)

        user = self.instance

        if department is None and user.position:
            user.position = None
            user.save()

        return value


class SendInviteSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)

    class Meta:
        fields = ('email',)


class PasswordResetSerializer(SendInviteSerializer):

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Пользователь с указанным email адресом отсутствует.'
            )
        return value


class PasswordResetConfirmSerializer(serializers.Serializer):

    reset_code = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    class Meta:
        fields = ('reset_code', 'password', 'password_confirm')

    def validate_password(self, value):
        password_confirm = self.initial_data.get('password_confirm')

        if password_confirm != value:
            raise serializers.ValidationError('Пароли не совпадают.')

        validate_password(value)
        return value


class PasswordChangeSerializer(serializers.Serializer):

    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    class Meta:
        fields = ('current_password', 'new_password', 'new_password_confirm')

    def validate_new_password(self, value):
        password_confirm = self.initial_data.get('new_password_confirm')

        if password_confirm != value:
            raise serializers.ValidationError('Пароли не совпадают.')

        validate_password(value)
        return value


class RegisterSerializer(serializers.Serializer):

    invite_code = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), required=True
    )
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(), required=True
    )

    class Meta:
        fields = ('invite_code', 'first_name',
                  'last_name', 'department', 'position', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate_position(self, value):
        department = self.initial_data.get('department')

        if department:
            if not value.departments.filter(pk=department).exists():
                raise serializers.ValidationError(
                    'Выбранная должность не относится к указанному отделу.'
                )

            if value.chief_position is True:
                raise serializers.ValidationError(
                    'Нельзя выбирать при регистрации руководящую должность.'
                )

        return value


class VerifyInviteSerializer(serializers.Serializer):

    invite_code = serializers.CharField(required=True)

    class Meta:
        fields = ('invite_code',)
