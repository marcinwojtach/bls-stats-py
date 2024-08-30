import io


class FileHelper:
    @staticmethod
    def create_buffer(figure, format='png'):
        buffer = io.BytesIO()
        figure.savefig(buffer, format=format)
        buffer.seek(0)
        return buffer
