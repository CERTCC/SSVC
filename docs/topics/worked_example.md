
# Worked Example

As an example, we will evaluate CVE-2018-14781 step by step from the deployer point of view.
The scenario here is that used for the pilot study.
This example uses the SSVC version 1 deployer decision tree.

The analyst’s first question is related to exploitation.
Technically, one could answer the questions in any order; however, exploitation is a good starting point because given
an adequately defined search procedure, one can always answer whether it finds an available exploit or proof of concept.
The scenario description for the pilot study reads as follows:

!!! info "State of exploitation"

    Metasploit and ExploitDB do not return results for this vulnerability. The NVD does not report any active exploitation of this vulnerability.

This information rules out “active” given the (perhaps limited) search procedure.
While the search did not produce a precise PoC, based on the description of the vulnerability, it is a fairly standard
traffic capture and replay attack that, given access to the transmission medium, should be straightforward to conduct
with Wireshark. Therefore, we select the “PoC” branch and then ask about exposure.
This considers the (fictional) deployer scenario blurb and the notional deployment of the affected system, as follows.

!!! info "Scenario blurb"

    We are a hospital that uses Medtronic devices frequently because of their quality and popularity in the market. We give these devices out to clients who need to monitor and track their insulin intake. If clients need to access data on their device, they can physically connect it to their computer or connect via Bluetooth to an app on their phone for monitoring capabilities. Occasionally, clients who use this device will have a doctor’s appointment in which the doctors have machines that can access the device as well to monitor or change settings. It is unknown how secure the doctor’s computer that interfaces directly with this insulin pump is. If the doctor’s computer is compromised, it potentially means that every device that connects to it is compromised as well. If an update to the insulin pump is required, a client can do this on their own through their computer or app or through a doctor while they are on-site at the hospital.

!!! info "Deployment of affected system"

    These pumps are attached directly to the client. If an update is required, the client is permitted to do that through their own computer or app. However, we have not provided them with documentation on properly using their computer or app to securely access their device. This is done for convenience so that if the user needs to change something quickly, they can. They can also come to us (hospital) for a change in their device’s settings for dosage etc. The doctor’s computer that directly handles interfacing with these devices is only connected to the intranet for the purpose of updating the client’s settings on the device. Doctors authenticate with ID badge and password.

[*System Exposure*](../reference/decision_points/system_exposure.md) is less straightforward than *Exploitation*.
The option [*open*](../reference/decision_points/system_exposure.md) is clearly ruled out.
However, it is not clear whether the optional Bluetooth connection between the medical device and a phone app represents
[*controlled*](../reference/decision_points/system_exposure.md) or [*small*](../reference/decision_points/system_exposure.md) exposure.
The description does not explicitly handle the capture/replay aspect of the vulnerability.
If the only way to exploit the vulnerability is to be within physical transmission range of the device, then that
physical constraint argues for exposure being [*small*](../reference/decision_points/system_exposure.md).
However, if the client’s phone app could be used to capture and replay attack packets, then unless that app is
particularly well secured, the answer should be [*controlled*](../reference/decision_points/system_exposure.md).
Regardless, the answer is not clear from the supplied information.
Furthermore, if this fictional app is specific to the insulin pump, then even if it is not compromised, the attack might
use its installation to remotely identify targets.
However, since most of the hospital’s clients have not installed the app, and for nearly all cases, physical proximity
to the device is necessary; therefore, we select [*small*](../reference/decision_points/system_exposure.md) and move on to ask about mission impact.

According to the fictional pilot scenario, “Our mission dictates that the first and foremost priority is to contribute
to human welfare and to uphold the Hippocratic oath (do no harm).” The continuity of operations planning for a hospital
is complex, with many MEFs.
However, even from this abstract, it seems clear that “do no harm” is at risk due to this vulnerability.
A mission essential function to that mission is each of the various medical devices works as expected, or at least if a
device fails, it cannot actively be used to inflict harm.
Unsolicited insulin delivery would mean that MEF “fails for a period of time longer than acceptable,” matching the
description of MEF failure.
The question is then whether the whole mission fails, which does not seem to be the case.
The recovery of MEF functioning is not affected, and most MEFs (the emergency services, surgery, oncology,
administration, etc.) would be unaffected.
Therefore, we select [*MEF failure*](../reference/decision_points/mission_impact.md) and move on to ask about safety impact.

This particular pilot study used SSVC version 1.
In the suggested deployer tree for SSVC version 2.1, mission and safety impact would be used to calculate the overall [*Human Impact*](../reference/decision_points/human_impact.md), and [*Automatable*](../reference/decision_points/automatable.md) would need to be answered as well.
Conducting further studies with the recommended version 2.1 Deployer tree remains an area of future work.
In the pilot study, this information is conveyed as follows:

!!! info "Use of the cyber-physical system"

    Insulin pumps are used to regulate blood glucose levels in diabetics.
    Diabetes is extremely common in the US.
    Misregulation of glucose can cause a variety of problems.
    Minor misregulation causes confusion or difficulty concentrating.
    Long-term minor mismanagement causes weigh management issues and blindness.
    Severe acute mismanagement can lead unconsciousness in a matter of minutes and death in a matter of hours.
    The impacted insulin pumps have a local (on-patient) wireless control, so wires to the pump do not have to be connected
    to the patient's control of the system, making the system lighter and less prone to be ripped out.

The closest match to “death in a matter of hours” would be [*hazardous*](../reference/decision_points/safety_impact.md) because that description reads
“serious or fatal injuries, where fatalities are plausibly preventable via emergency services or other measures.”
Depending on the details of the hospital’s contingency plans and its monitoring of their patients, the
[*Safety Impact*](../reference/decision_points/safety_impact.md) could be [*catastrophic*](../reference/decision_points/safety_impact.md).
If there is no way to tell whether the insulin pumps are misbehaving, for example, then exploitation could go on for
some time, leading to a [*catastrophic*](../reference/decision_points/safety_impact.md) [*Safety Impact*](../reference/decision_points/safety_impact.md).
The pilot information is inadequate in this regard, which is the likely source of disagreement about
[*Safety Impact*](../reference/decision_points/safety_impact.md) in Table 13.
For the purposes of this example, imagine that after gathering that information, the monitoring situation is adequate,
and select [*hazardous*](../reference/decision_points/safety_impact.md).
Therefore, mitigate this vulnerability *out-of-cycle*, meaning that it should be addressed quickly, ahead of the usual
update and patch cycle.
