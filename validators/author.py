

class AuthorValidator(object):

    @classmethod
    def author_key_validators(cls, author_key):
        errors = []

        if not author_key:
            errors.append("news must contain 'author_key' string objectId")

        if author_key and not isinstance(author_key, str):
            errors.append("'author_key' type must be string key, ex:'5fbc850015eb9bbca94c209b' ")

        return author_key, errors

    @classmethod
    def author_name_validators(cls, name):
        errors = []

        if not name:
            errors.append("author must contain 'name' string")

        if name and not isinstance(name, str):
            errors.append("'name' type must be string")

        if name and len(name) > 50:
            errors.append("'name' string must be maximum length of 50")

        return name, errors
