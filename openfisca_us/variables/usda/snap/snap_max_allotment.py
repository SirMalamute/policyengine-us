from openfisca_us.model_api import *


class snap_max_allotment(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    documentation = "Maximum SNAP allotment for SPM unit, based on the state group and household size."
    label = "SNAP maximum allotment"
    unit = USD

    def formula(spm_unit, period, parameters):
        max_allotments = parameters(period).usda.snap.max_allotment.main
        state_group = spm_unit.household("state_group_str", period)
        household_size = spm_unit("spm_unit_size", period)
        return max_allotments[state_group][household_size] * 12
