class Utils:
    @staticmethod
    def get_error_message(exception):
        if exception.__cause__:
            return str(exception.__cause__)
        else:
            return str(exception)