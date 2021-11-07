from rest_framework import serializers

from authentication.models import User

from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializing user registration and creating a new one. """
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Use the create_user method that we
        # written earlier to create a new user.
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def create(self, data):
        # In the validate method, we make sure that the current instance
        # LoginSerializer value valid. If a user is logged in
        # this means confirmation that an email address is present
        # mail and that this combination matches one of the users.
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class UserSerializer(serializers.ModelSerializer):
    """ It serializes and deserializes User objects. """

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        """ Update User. """

        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            # For the keys remaining in validated_data, we set the values
            # into the current User instance one by one
            setattr(instance, key, value)

        if password is not None:
            # 'set_password()' solves all issues related to security
            #  when updating the password.
            instance.set_password(password)

        instance.save()
        return instance
