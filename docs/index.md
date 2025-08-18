# Stakeholder-Specific Vulnerability Categorization

SSVC stands for A Stakeholder-Specific Vulnerability Categorization.
It is a methodology for prioritizing vulnerabilities based on the needs of the stakeholders involved in the vulnerability management process.
SSVC is designed to be used by any stakeholder in the vulnerability management process, including finders, vendors, coordinators, deployers, and others.

## Where to go from here

We have organized the SSVC documentation into four main sections:

<div class="grid cards" markdown>

- :fontawesome-regular-eye:{ .lg .middle } **SSVC Overview**

    ---

    A beginner's guide to SSVC.
    This section is for people who have never heard of SSVC.

    [:octicons-arrow-right-24: An Overview of SSVC](ssvc_overview.md)

- :material-clipboard-check:{ .lg .middle } **SSVC How To**

    ---

    Start using SSVC in your organization today with step-by-step instructions.
    This section is intended for people who are already familiar with SSVC and want to start using it.

    [:octicons-arrow-right-24: SSVC How To](howto/index.md)

- :fontawesome-solid-book:{ .lg .middle } **More about SSVC**

    ---

    Dig deeper to understand the SSVC methodology and how it works.
    This section is intended for people who are already familiar with SSVC and want to learn more.

    [:octicons-arrow-right-24: Understanding SSVC](topics/index.md)

- :material-book-open-page-variant:{ .lg .middle } **SSVC Reference**

    ---

    Reference documentation for SSVC.
    This section is intended for people who are already familiar with SSVC and want to look up specific details.

    [:octicons-arrow-right-24: Reference](reference/index.md)

</div>

{% include-markdown "_includes/helping_out.md" heading-offset=1 %}


```mermaid
flowchart LR
    ReportPublicStatus_1{ReportPublicStatus}
    SupplierContactedStatus_2{SupplierContactedStatus}
    ReportPublicStatus_1 -->|True| SupplierContactedStatus_2
    ReportCredibilityLevel_3{ReportCredibilityLevel}
    SupplierContactedStatus_2 -->|True| ReportCredibilityLevel_3
    SupplierCardinalityLevel_4{SupplierCardinalityLevel}
    ReportCredibilityLevel_3 -->|CREDIBLE| SupplierCardinalityLevel_4
    UtilityLevel_5{UtilityLevel}
    SupplierCardinalityLevel_4 -->|MULTIPLE| UtilityLevel_5
    PublicSafetyImpactLevel_6{PublicSafetyImpactLevel}
    UtilityLevel_5 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_6
    Action_COORDINATE_7[COORDINATE]
    PublicSafetyImpactLevel_6 -->|SIGNIFICANT| Action_COORDINATE_7
    Action_TRACK_8[TRACK]
    PublicSafetyImpactLevel_6 -->|MINIMAL| Action_TRACK_8
    PublicSafetyImpactLevel_9{PublicSafetyImpactLevel}
    UtilityLevel_5 -->|EFFICIENT| PublicSafetyImpactLevel_9
    Action_TRACK_10[TRACK]
    PublicSafetyImpactLevel_9 -->|SIGNIFICANT| Action_TRACK_10
    Action_DECLINE_11[DECLINE]
    PublicSafetyImpactLevel_9 -->|MINIMAL| Action_DECLINE_11
    Action_DECLINE_12[DECLINE]
    UtilityLevel_5 -->|LABORIOUS| Action_DECLINE_12
    UtilityLevel_13{UtilityLevel}
    SupplierCardinalityLevel_4 -->|ONE| UtilityLevel_13
    PublicSafetyImpactLevel_14{PublicSafetyImpactLevel}
    UtilityLevel_13 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_14
    Action_TRACK_15[TRACK]
    PublicSafetyImpactLevel_14 -->|SIGNIFICANT| Action_TRACK_15
    Action_DECLINE_16[DECLINE]
    PublicSafetyImpactLevel_14 -->|MINIMAL| Action_DECLINE_16
    Action_DECLINE_17[DECLINE]
    UtilityLevel_13 -->|EFFICIENT| Action_DECLINE_17
    Action_DECLINE_18[DECLINE]
    UtilityLevel_13 -->|LABORIOUS| Action_DECLINE_18
    Action_DECLINE_19[DECLINE]
    ReportCredibilityLevel_3 -->|NOT_CREDIBLE| Action_DECLINE_19
    SupplierCardinalityLevel_20{SupplierCardinalityLevel}
    SupplierContactedStatus_2 -->|False| SupplierCardinalityLevel_20
    UtilityLevel_21{UtilityLevel}
    SupplierCardinalityLevel_20 -->|MULTIPLE| UtilityLevel_21
    PublicSafetyImpactLevel_22{PublicSafetyImpactLevel}
    UtilityLevel_21 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_22
    Action_COORDINATE_23[COORDINATE]
    PublicSafetyImpactLevel_22 -->|SIGNIFICANT| Action_COORDINATE_23
    Action_TRACK_24[TRACK]
    PublicSafetyImpactLevel_22 -->|MINIMAL| Action_TRACK_24
    Action_DECLINE_25[DECLINE]
    UtilityLevel_21 -->|EFFICIENT| Action_DECLINE_25
    Action_DECLINE_26[DECLINE]
    UtilityLevel_21 -->|LABORIOUS| Action_DECLINE_26
    Action_DECLINE_27[DECLINE]
    SupplierCardinalityLevel_20 -->|ONE| Action_DECLINE_27
    SupplierContactedStatus_28{SupplierContactedStatus}
    ReportPublicStatus_1 -->|False| SupplierContactedStatus_28
    ReportCredibilityLevel_29{ReportCredibilityLevel}
    SupplierContactedStatus_28 -->|True| ReportCredibilityLevel_29
    SupplierCardinalityLevel_30{SupplierCardinalityLevel}
    ReportCredibilityLevel_29 -->|CREDIBLE| SupplierCardinalityLevel_30
    SupplierEngagementLevel_31{SupplierEngagementLevel}
    SupplierCardinalityLevel_30 -->|MULTIPLE| SupplierEngagementLevel_31
    UtilityLevel_32{UtilityLevel}
    SupplierEngagementLevel_31 -->|ACTIVE| UtilityLevel_32
    PublicSafetyImpactLevel_33{PublicSafetyImpactLevel}
    UtilityLevel_32 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_33
    Action_COORDINATE_34[COORDINATE]
    PublicSafetyImpactLevel_33 -->|SIGNIFICANT| Action_COORDINATE_34
    Action_TRACK_35[TRACK]
    PublicSafetyImpactLevel_33 -->|MINIMAL| Action_TRACK_35
    PublicSafetyImpactLevel_36{PublicSafetyImpactLevel}
    UtilityLevel_32 -->|EFFICIENT| PublicSafetyImpactLevel_36
    Action_TRACK_37[TRACK]
    PublicSafetyImpactLevel_36 -->|SIGNIFICANT| Action_TRACK_37
    Action_TRACK_38[TRACK]
    PublicSafetyImpactLevel_36 -->|MINIMAL| Action_TRACK_38
    Action_TRACK_39[TRACK]
    UtilityLevel_32 -->|LABORIOUS| Action_TRACK_39
    UtilityLevel_40{UtilityLevel}
    SupplierEngagementLevel_31 -->|UNRESPONSIVE| UtilityLevel_40
    PublicSafetyImpactLevel_41{PublicSafetyImpactLevel}
    UtilityLevel_40 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_41
    Action_COORDINATE_42[COORDINATE]
    PublicSafetyImpactLevel_41 -->|SIGNIFICANT| Action_COORDINATE_42
    Action_TRACK_43[TRACK]
    PublicSafetyImpactLevel_41 -->|MINIMAL| Action_TRACK_43
    Action_TRACK_44[TRACK]
    UtilityLevel_40 -->|EFFICIENT| Action_TRACK_44
    Action_DECLINE_45[DECLINE]
    UtilityLevel_40 -->|LABORIOUS| Action_DECLINE_45
    SupplierEngagementLevel_46{SupplierEngagementLevel}
    SupplierCardinalityLevel_30 -->|ONE| SupplierEngagementLevel_46
    UtilityLevel_47{UtilityLevel}
    SupplierEngagementLevel_46 -->|ACTIVE| UtilityLevel_47
    PublicSafetyImpactLevel_48{PublicSafetyImpactLevel}
    UtilityLevel_47 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_48
    Action_TRACK_49[TRACK]
    PublicSafetyImpactLevel_48 -->|SIGNIFICANT| Action_TRACK_49
    Action_TRACK_50[TRACK]
    PublicSafetyImpactLevel_48 -->|MINIMAL| Action_TRACK_50
    Action_TRACK_51[TRACK]
    UtilityLevel_47 -->|EFFICIENT| Action_TRACK_51
    Action_DECLINE_52[DECLINE]
    UtilityLevel_47 -->|LABORIOUS| Action_DECLINE_52
    Action_DECLINE_53[DECLINE]
    SupplierEngagementLevel_46 -->|UNRESPONSIVE| Action_DECLINE_53
    Action_DECLINE_54[DECLINE]
    ReportCredibilityLevel_29 -->|NOT_CREDIBLE| Action_DECLINE_54
    SupplierCardinalityLevel_55{SupplierCardinalityLevel}
    SupplierContactedStatus_28 -->|False| SupplierCardinalityLevel_55
    UtilityLevel_56{UtilityLevel}
    SupplierCardinalityLevel_55 -->|MULTIPLE| UtilityLevel_56
    PublicSafetyImpactLevel_57{PublicSafetyImpactLevel}
    UtilityLevel_56 -->|SUPER_EFFECTIVE| PublicSafetyImpactLevel_57
    Action_COORDINATE_58[COORDINATE]
    PublicSafetyImpactLevel_57 -->|SIGNIFICANT| Action_COORDINATE_58
    Action_TRACK_59[TRACK]
    PublicSafetyImpactLevel_57 -->|MINIMAL| Action_TRACK_59
    Action_DECLINE_60[DECLINE]
    UtilityLevel_56 -->|EFFICIENT| Action_DECLINE_60
    Action_DECLINE_61[DECLINE]
    UtilityLevel_56 -->|LABORIOUS| Action_DECLINE_61
    Action_DECLINE_62[DECLINE]
    SupplierCardinalityLevel_55 -->|ONE| Action_DECLINE_62
```