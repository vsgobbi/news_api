

class NewsValidator(object):

    @classmethod
    def title_validators(cls, title):
        errors = []

        if not title:
            errors.append("news must contain 'title' string")

        if title and not isinstance(title, str):
            errors.append("'title' type must be string")

        if title and len(title) > 150:
            errors.append("'title' string must be maximum length of 150")

        return title, errors

    @classmethod
    def content_validators(cls, content):
        errors = []

        if not content:
            errors.append("news must contain 'content' string")

        if content and not isinstance(content, str):
            errors.append("'content' type must be string")

        return content, errors
