from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted

class ActionFornecerSuporte(Action):
    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Captura a entidade 'problema' da mensagem
        problema = next(tracker.get_latest_entity_values("problema"), None)
        
        # Mapeamento de soluções
        solucoes = {
            "acesso": "utter_solucao_acesso",
            "login": "utter_solucao_acesso",
            "conta": "utter_solucao_acesso",
            "plano": "utter_solucao_plano",
            "assinatura": "utter_solucao_plano",
            "tecnico": "utter_solucao_tecnico",
            "erro": "utter_solucao_tecnico",
            "bug": "utter_solucao_tecnico"
        }

        response = solucoes.get(problema, "utter_encaminhar_humano")
        dispatcher.utter_message(response=response)
        
        return [SlotSet("problema", problema)]

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [Restarted()]