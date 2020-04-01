from classes.creatures.item.skill import Skill

class Skills:
    kick		= Skill('kick',  'Удар ногой',   'Отмашистый удар ногой', attack=5, cost=10)
    beat		= Skill('beat',  'Удар кулаком', 'Не сильный удар',       attack=3, cost=5)
    remana		= Skill('remana','Медитация',    'Восстанавливает ману',  remana=5, cost=7)