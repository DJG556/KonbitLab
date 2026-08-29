from abc import ABC,abstractmethod

class Personne(ABC):
    
    nb_inst = 0
    def __init__(self, nom, prenom, sexe, age):
            
            self.nom=nom
            self.prenom=prenom
            self.sexe=sexe
            self.age=age
            Personne.nb_inst+=1
            self.id =Personne.nb_inst
            
    def __str__(self):
        return f"{self.nom} {self.prenom} => {self.sexe} ,"
        #   ===================== AFFICHER ===============
    def afficher(self):
            print("="*20)
            print(f"\t ID : {self.id}")
            print(f"\t Nom : {self.nom}")
            print(f"\t Prenom : {self.prenom}") 
            print(f"\t Sexe : {self.sexe}") 
            print(f"\t Age : {self.age} ans")  
            print("="*20)
        #   ===================== SE PRESENTER ===============
    @abstractmethod
    def parler(self):
        return f"Bonjour"
    def Sepresenter(self):
        if self.sexe.lower() == "m":
            return f"Je suis M. {self.nom} {self.prenom}. \nJ'ai {self.age} ans."
        elif self.sexe.lower() =="f":
            return f"Je suis Mme/Mlle {self.nom} {self.prenom} \nJ'ai {self.age} ans."        
        else:
            return "Vous devez specifier un sexe normal"   
        
    @classmethod
    def totale_instances(cls):
        print(f"Nombre instances existant : {Personne.nombre_instances}")

    @classmethod
    def derniere_instances(cls):
        print(f"l'Id de la derniere instance  est: {Personne.nombre_instances}") 
        
    
class Etudiant(Personne):
    #================== Redefinition de la methode constructeur ====================
    def __init__(self, nom, prenom, sexe, age, faculte, nivaeu):
        super().__init__(nom, prenom, sexe, age)
        self.faculte = faculte
        self.niveau = nivaeu

    def __str__(self):
        return super().__str__() + f" Faculté : {self.faculte} | Niveau : {self.niveau}"
    
    #================= Redefinition de la methode se_presenter ===================
    def se_presenter(self):
        return super().se_presenter() + f" \n Je suis en niveau {self.niveau} a la faculte {self.faculte}"

    #================== Redefinition de la methode afficher ====================
    def afficher(self):
        super().afficher()   
        print(f"\t Faculte : {self.faculte}") 
        print(f"\t Niveau : {self.niveau}")  
        print("="*20)
    
    
class Employer(Personne):
    
    #================== Redefinition de la methode constructeur ====================
    def __init__(self, nom, prenom, sexe, age, fonction, salaire):
        super().__init__(nom, prenom, sexe, age)
        self.fonction=fonction
        self.salaire=salaire 
        
    def __str__(self):
        return super().__str__() + f" Fonction: {self.fonction} | Salaire : {self.salaire}"
    #================= Redefinition de la methode se_presenter ===================   
    def Sepresenter(self):
        return super().Sepresenter() + f"\nMa fonction est {self.fonction} j'ai un salaire de {self.salaire} HTG"
    
    #================== Redefinition de la methode afficher ====================
    def afficher(self):
        super().afficher()   
        print(f"\t Fonction : {self.fonction}") 
        print(f"\t Salaire : {self.salaire} HTG")  
        print("="*20)
    #================== Methode Embaucher ==================
    def embaucher(self):
        return f"\nL'employé(e) {self.nom} {self.prenom} a été embauché(e) comme {self.fonction} avec un salaire de {self.salaire} HTG."
    
class Enseignant(Personne):
    
    #================== Redefinition de la methode constructeur ====================
    def __init__(self, nom, prenom, sexe, age, specialite, taux_horaire):
        super().__init__(nom, prenom, sexe, age)
        self.specialite=specialite
        self.taux_horaire=taux_horaire
    
    
    def __str__(self):
        return super().__str__() + f" Specialite: {self.specialite} | Toux Horaire : {self.taux_horaire}"
    #================= Redefinition de la methode se_presenter ===================    
    def Sepresenter(self):
        return super().Sepresenter() + f"\nMa spécialité est {self.specialite} et j'ai une taux horaire de {self.taux_horaire} HTG"
    
    #================== Redefinition de la methode afficher ====================
    def afficher(self):
        super().afficher()   
        print(f"\t Spécialité : {self.specialite}") 
        print(f"\t Taux Horaire : {self.taux_horaire} HTG/H")  
        print("="*20)
    
    #================== Methode contracter ==================== 
    def contracter(self):
        return f"\nLa specialité de l'enseignant(e) {self.nom} {self.prenom} est '{self.specialite}' et son taux horaire est de {self.taux_horaire} HTG"
        
