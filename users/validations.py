from django.core.validators import RegexValidator

PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&_-])[A-Za-z\d@$!%*#?&_-]{8,}$'

PASSWORD_REGEX_VALIDATOR = RegexValidator(
    regex=PASSWORD_REGEX,
    message="Minimum eight characters, at least one letter, one number and one special character",
)
