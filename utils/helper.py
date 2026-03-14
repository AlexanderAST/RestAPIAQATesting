import allure
import json

from allure_commons.types import AttachmentType

class Helper:
    
    #передается респонс берется джсон и прикрепляет ответ к аллюр отчету
    def attach_resonce(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Responce", attachment_type=AttachmentType.JSON)