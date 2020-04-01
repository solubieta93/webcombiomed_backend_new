from rest_framework.parsers import FileUploadParser
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class FilesView(GenericViewSet):
    parser_classes = [FileUploadParser]

    def __init__(self, folder_name='file', **kwargs):
        super().__init__(**kwargs)
        self.folder_name = folder_name

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)

    @action(methods=['post'], detail=False)  # , url_path='images', url_name='images')
    def upload(self, request):
        file_obj = request.data['file']

        return Response(
            data=
            {

                'id': 1233243,
                'url': ''
            },
            status=201)

