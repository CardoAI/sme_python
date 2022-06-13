from abc import ABC, abstractmethod


class BlobStorageClient(ABC):

    @abstractmethod
    def save_data(self, data):
        pass


class S3BlobStorageClient(BlobStorageClient):

    def save_data(self, data):
        return 'https://mercurydbdump.s3.eu-central-1.amazonaws.com/sme_dumps/opyn_companies.json?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aDGV1LWNlbnRyYWwtMSJGMEQCIC7VBtNQ63ojYNMue%2BjTW1hWb6uyf0sRaX6h75gG%2BtABAiAQcMAsNZfFbfKZLaRGYHXUcxP1ZgYXDzeeMm6of2Qj4CqBAwhoEAMaDDEzOTc3MzczOTcwNyIMPq%2Fkv8qz6lkIX5PlKt4Ci2ljeM%2FbLX0rIxwTiBSBiEUn2LcNsf94NAdGSAN8eKjbtWWN74EMFmXbze2gKQ%2BYsGdGdLXYYX6oMy3VD8v1Cz36as%2BNwUKIb3Vh3u6EF8%2BMJPwpO0gGq7aKaU2AIbeIHuMz%2BXKtGpEHsC40d3H6NjWVBkKVeCsLgWBrUdK9bQLfKzsjoLV3tKYqDqKOljz9QyKl3Mqy%2FN3zKOk4WaAY4O6IQ3AGHeD14nRsylWlCv5vIPERjyULitCgYmx83UaWl93PYzvQ%2F5jS92jl3MnM16kA7zfE%2BANI7%2FIq7XRUWN8sbHA2HYuR%2F1v%2BNzPipmv7b7VLSO1cJpGVvZrk6C2zdVKB5fJpHOh9P7j1s9kPd64jva%2FeerXAD2eWsAoxSwR8Xw6Jb5sLiBk%2FnBpzeb1DcFiTvSP5Vnsh91%2Fz%2FeKuXbyL56%2FPGsI2gdQSmLDpwjmGP2RqgV3UcSQbESz%2FPpIwhNuZlQY6tAItK6Jke1YVRLwAjDNoNlodPVkCx7LFRIBrf9B2uXt7MeSsGPPa4eFMWVC0%2F62fFRpTr5sz8RZH6ujMBzZPulc3pwUOZffF8eIOJ23tlTeXh8w3D0FR%2FrSaP0gAB6keVQZxTAsJnjWiJjbZkNPkHH2iK7HClLnVZTH6bHymbAJPBRIRUlraFvAXRJFlqZzM8rk2RcAQLiH50neKsiGZ1hG7UX1ftty7f4zslbuTaJaDmPJZEygtGVmYTUZRO2kTH39QFXdMeOGxQkkujvYm6mfiaa48j4BJ%2BVfBh4daqkGRf4bjNcOzg9WLhJStwUt9ifjRRCttNp1skvA9RpbwO7b%2BfxDs%2B7qNGSLkr5dtnJ5PvIl8qN%2FLG8GGEGe6nqTJzQ8KPGlsbeUIQaMdxJ3qFWL9709xMg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220612T225054Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIASBCZKAK5YHJEBBGI%2F20220612%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Signature=3fb2e331ed690e139345fba72e4d873d3052f67e48172979720a5ad5746b219e'
