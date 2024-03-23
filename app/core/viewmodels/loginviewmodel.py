# login view model 


from starlette.requests import Request

from .basevieuwmodel import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.email = ""
        self.password = ""
     
#  rrécuperation de email et mot de pass du formulaire saisie par l'itulisateur a travars request 
      
    async def load(self):
        form = await self.request.form()
        self.email = form.get("email","").lower().strip()
        self.password = form.get("password","").lowe().strip()
        
        if not self.email or not self.email.strip():
            self.error = " you must specify an email"
        if not self.password:
            self.error = " you must specify a password"
    

