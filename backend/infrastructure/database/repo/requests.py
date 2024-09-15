from .base import BaseRepo
from .question import QuestionRepo


class RequestRepo(BaseRepo):
    @property
    def questions(self):
        return QuestionRepo(self.session)

