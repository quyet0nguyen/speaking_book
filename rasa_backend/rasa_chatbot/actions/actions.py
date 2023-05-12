from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionVoTuyenKPIServiceProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_KPI_SERVICE_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:


        entities = tracker.latest_message['entities']

        text = "Bắt được chất lượng dịch vụ di động tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Voice_CSSR: x" + "\n" \
            + "\t" + "Voice_CDR: x" + "\n" \
            + "\t" + "Data_CSSR: x" + "\n" \
            + "\t" + "Data_CDR: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenSCR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SCR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn kênh báo hiệu SCR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "SCR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenKPI3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_KPI_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được chất lượng mạng 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CS_CSSR: x" + "\n" \
            + "\t" + "CS_CDR: x" + "\n" \
            + "\t" + "PS_CSSR: x" + "\n" \
            + "\t" + "PS_CDR: x" + "\n" \
            + "\t" + "RRC_CR: x" + "\n" \
            + "\t" + "RAB_CS_CR: x" + "\n" \
            + "\t" + "RAB_PS_CR: x"

        dispatcher.utter_message(text = text)   

        return []

class ActionVoTuyenCSRABCR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CS_RAB_CR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn CS_RAB_CR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CS_RAB_CR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []

class ActionVoTuyenSUBAttachedCell(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SUB_ATTACHED_CELL"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số thuê bao attached tại cell " + str(entities[0]['value']) + "\n" \
            + "\t" + "Số thuê bao Attached là: x"    

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenCSFBSRLTE4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CSFB_SR_LTE_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ CSFB_SR_LTE 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CSFB_SR_LTE_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []

class ActionVoTuyenEPSCSSR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_EPS_CSSR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập phiên data thành công ePS_CSSR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "ePS_CSSR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenSDR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SDR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt kênh báo hiệu SDR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "SDR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenVoiceCDRProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_VOICE_CDR_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt cuộc gọi thoại VoiCe_CDR tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "VoiCe_CDR: x" + "\n" \
            + "\t" + "So với CTKT: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenTCR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_TCR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn kênh thoại TCR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "TCR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenHOSR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_HOSR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ chuyển giao thành công HOSR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "HOSR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenVolteCSSR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_VOLTE_CSSR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập cuộc gọi thoại thành công VoLTE_CSSR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "VoLTE_CSSR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenCSSR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CSSR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập cuộc gọi thành công CSSR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CSSR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenSoCellPSProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SOCELL_PS_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số cell phát sóng tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Tổng số cell đang PS: x" + "\n" \
            + "\t" + "Tổng số cell 2G đang PS: x" + "\n" \
            + "\t" + "Tổng số cell 3G đang PS: x" + "\n" \
            + "\t" + "Tổng số cell 4G đang PS: x" + "\n" \
            + "\t" + "Tổng số cell 5G đang PS: x"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenErabCR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_ERAB_CR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn eRAB_CR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "eRAB_CR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenTramDoiThuProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_TRAMDOITHU_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số trạm đối thủ tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Số trạm của đối thủ Vinaphone: x " \
            + "\t" + "Số trạm của đối thủ Mobifone: x" + "\n" \
            + "\t" + "Số trạm của đối thủ Vietnam Mobile: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenKPI2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_KPI_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được chất lượng mạng 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CSSR: x" + "\n" \
            + "\t" + "CDR: x" + "\n" \
            + "\t" + "TCR: x" + "\n" \
            + "\t" + "SCR: x" + "\n" \
            + "\t" + "TCR: x" + "\n" \
            + "\t" + "HOSR: x" + "\n" \
            + "\t" + "SDR: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenPSCDR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_PS_CDR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt phiên data PS_CDR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "PS_CDR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenDataCDRProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_DATA_CDR_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt phiên data Data_CDR tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Data_CDR: x" + "\n" \
            + "\t" + "So với CTKT: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenRRCCR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_RRC_CR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn RRC_CR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "RRC_CR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenPSRABCR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_PS_RAB_CR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn PS_RAB_CR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "PS_RAB_CR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
    
class ActionVoTuyenSUBAttachedTram(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SUB_ATTACHED_TRAM"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số thuê bao attached tại trạm " + str(entities[0]['value']) + "\n" \
            + "\t" + "Số thuê bao Attached là: x"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenEPSCDR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_EPS_CDR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt phiên data ePS_CDR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "ePS_CDR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionKPICell(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_KPI_CELL"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        # text = "Bắt được tỉ lệ CSFB_SR_LTE 4G tại " + str(entities[0]['value']) + "\n" \
        #     + "\t" + "CSFB_SR_LTE_4G: x" + "\n" \
        #     + "\t" + "So với ngày trước: x" + "\n" \
        #     + "\t" + "So với tuần trước: x" 

        text = "Chưa có response"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenSubAttachedProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SUB_ATTACHED_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số thuê bao attached tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Tổng số thuê bao Attached: x" + "\n" \
            + "\t" + "Số thuê bao attached 2G: x" + "\n" \
            + "\t" + "Số thuê bao attached 3G: x" + "\n" \
            + "\t" + "Số thuê bao attached 4G: x" + "\n" \
            + "\t" + "Tỷ trọng thuê bao 2G: x" + "\n" \
            + "\t" + "Tỷ trọng thuê bao 3G: x" + "\n" \
            + "\t" + "Tỷ trọng thuê bao 4G: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenSoTramPSProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_SOTRAM_PS_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được số vị trí trạm phát sóng tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Tổng số vị trí trạm đang PS: x" + "\n" \
            + "\t" + "Tổng số vị trí trạm 2G đang PS: x" + "\n" \
            + "\t" + "Tổng số vị trí trạm 3G đang PS: x" + "\n" \
            + "\t" + "Tổng số vị trí trạm 4G đang PS: x" + "\n" \
            + "\t" + "Tổng số vị trí trạm 5G đang PS: x"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenDataCSSRProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_DATA_CSSR_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập phiên data thành công Data_CSSR tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Data_CSSR: x" + "\n" \
            + "\t" + "So với CTKT: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenTuProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_TU_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được hiệu suất sử dụng mạng tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "TUnonHR_2G: x" + "\n" \
            + "\t" + "TUHR80_2G: x" + "\n" \
            + "\t" + "TU_Traffic_3G: x" + "\n" \
            + "\t" + "TU_Traffic_4G: x" + "\n" \
            + "\t" + "TU_PRB_DL: x" + "\n" \
            + "\t" + "TTU_PRB_UL: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenERRCCR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_ERRC_CR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ nghẽn eRRC_CR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "eRRC_CR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenVolteCDR4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_VOLTE_CDR_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt cuộc gọi thoại VoLTE_CDR 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "VoLTE_CDR_4G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenThroughputProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_THROUGHPUT_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tốc độ tải xuống của người dùng tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "DL_User_Throughput_3G_Mbps: x" + "\n" \
            + "\t" + "DL_User_Throughput_4G_Mbps: x"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenCSCDR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CS_CDR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt cuộc gọi thoại CS_CDR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CS_CDR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenCSCSSR3Grovince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CS_CSSR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập cuộc gọi thoại thành công CS_CSSR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CS_CSSR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenPSCSSR3GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_PS_CSSR_3G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập phiên data thành công PS_CSSR 3G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + " PS_CSSR_3G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenTrafficProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_TRAFFIC_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được lưu lượng tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CSFB_SR_LTE_4G: x" + "\n" \
            + "\t" + "Tổng lưu lượng thoại (Erl): x" + "\n" \
            + "\t" + "Lưu lượng thoại 2G (Erl): x" + "\n" \
            + "\t" + "Lưu lượng thoại 3G (Erl): x" + "\n" \
            + "\t" + "Lưu lượng thoại 4G (Erl): x" + "\n" \
            + "\t" + "Tỷ trọng lưu lượng thoại 2G: x" + "\n" \
            + "\t" + "Tỷ trọng lưu lượng thoại 3G: x" + "\n" \
            + "\t" + "Tỷ trọng lưu lượng thoại 4G: x" + "\n" \
            + "\t" + "Total_Data_Traffic_GB: x" + "\n" \
            + "\t" + "Lưu lượng data 3G (GB): x" + "\n" \
            + "\t" + "Lưu lượng data 4G (GB): x" + "\n" \
            + "\t" + "Tỷ trọng lưu lượng data 3G: x" + "\n" \
            + "\t" + "Tỷ trọng lưu lượng data 4G: x" 

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenCDR2GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_CDR_2G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ rớt cuộc gọi CDR 2G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "CDR_2G: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x"

        dispatcher.utter_message(text = text)   

        return []
    
class ActionVoTuyenKPI4GProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_KPI_4G_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được chất lượng mạng 4G tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "ePS_CSSR: x" + "\n" \
            + "\t" + "ePS_CDR: x" + "\n" \
            + "\t" + "VoLTE_CSSR: x" + "\n" \
            + "\t" + "VoLTE_CDR: x" + "\n" \
            + "\t" + "eRRC_CR: x" + "\n" \
            + "\t" + "eRAB_CR: x" + "\n" \
            + "\t" + "CSFB SR LTE: x"

        dispatcher.utter_message(text = text)   

        return []

class ActionVoTuyenDataCSSRProvince(Action):

    def name(self) -> Text:
        return "action_VOTUYEN_DATA_CSSR_PROVINCE"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        text = "Bắt được tỉ lệ thiết lập phiên data thành công Data_CSSR tại " + str(entities[0]['value']) + "\n" \
            + "\t" + "Data_CSSR: x" + "\n" \
            + "\t" + "So với CTKT: x" + "\n" \
            + "\t" + "So với ngày trước: x" + "\n" \
            + "\t" + "So với tuần trước: x"

        dispatcher.utter_message(text = text)   

        return []