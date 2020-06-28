from house_info import HouseInfo

from datetime import date

class EnergyData(HouseInfo):
    ENERGY_PER_BULB = 0.2
    ENERGY_BITS = 0X0F0


    def _get_energy(self, rec):
        energy = int(rec,base=16)
        energy = energy and ENERGY_BITS


        return recs

        # <editor-fold desc="Description">
        def get_data_by_area(self, rec_area = 0):
            recs = super().get_data_by_area("particulate", rec_area)
            return self._convert_data(recs)

        def get_data_by_date(self, rec_date=date.today()):
            recs = super().get_data_by_date("particulate", rec_date)
            return self._convert_data(recs)

        def get_data_concentrations(self, data):
            particulate = {"good": 0,"moderate": 0,"bad": 0}
            for rec in data:
                if rec <=50.0:
                    particulate["good"] += 1
                elif rec > 50.0 and rec <= 100.0:
                    particulate["moderate"] +=1
                else:
                    particulate["bad"] += 1
            return particulate
        # </editor-fold>
