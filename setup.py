#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kenneth T. Moore',
 'author_email': 'kenneth.t.moore-1@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO component wrapper for FLOPS',
 'download_url': '',
 'entry_points': '[openmdao.component]\nflops_wrapper.flops_wrapper.FlopsWrapper=flops_wrapper.flops_wrapper:FlopsWrapper\n\n[openmdao.container]\nflops_wrapper.flops_wrapper.FlopsWrapper_input_confin=flops_wrapper.flops_wrapper:FlopsWrapper_input_confin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_MSJet=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_MSJet\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Inertia=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Inertia\nflops_wrapper.flops_wrapper.FlopsWrapper_input_syntin=flops_wrapper.flops_wrapper:FlopsWrapper_input_syntin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Fuselage=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Fuselage\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Plot_Files=flops_wrapper.flops_wrapper:FlopsWrapper_output_Plot_Files\nflops_wrapper.flops_wrapper.FlopsWrapper_input_costin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_costin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin_Thrust_Reverser=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin_Thrust_Reverser\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Shielding=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Shielding\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_OEW_Calculations=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_OEW_Calculations\nflops_wrapper.flops_wrapper.FlopsWrapper_input_option=flops_wrapper.flops_wrapper:FlopsWrapper_input_option\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin_Takeoff=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin_Takeoff\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_rfhin=flops_wrapper.flops_wrapper:FlopsWrapper_input_rfhin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_costin=flops_wrapper.flops_wrapper:FlopsWrapper_input_costin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Center_of_Gravity=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Center_of_Gravity\nflops_wrapper.flops_wrapper.FlopsWrapper_input_option_Program_Control=flops_wrapper.flops_wrapper:FlopsWrapper_input_option_Program_Control\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Store_Drag=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Store_Drag\nflops_wrapper.flops_wrapper.FlopsWrapper_input_aerin_Internal_Aero=flops_wrapper.flops_wrapper:FlopsWrapper_input_aerin_Internal_Aero\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Ground_Effects=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Ground_Effects\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Propagation=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Propagation\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Detailed_Wing=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Detailed_Wing\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Performance_Constraints=flops_wrapper.flops_wrapper:FlopsWrapper_output_Performance_Constraints\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine\nflops_wrapper.flops_wrapper.FlopsWrapper_input_confin_Design_Variables=flops_wrapper.flops_wrapper:FlopsWrapper_input_confin_Design_Variables\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Cruise=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Cruise\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Econ=flops_wrapper.flops_wrapper:FlopsWrapper_output_Econ\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_Design_Point=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_Design_Point\nflops_wrapper.flops_wrapper.FlopsWrapper_input_option_Plot_Files=flops_wrapper.flops_wrapper:FlopsWrapper_input_option_Plot_Files\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Performance=flops_wrapper.flops_wrapper:FlopsWrapper_output_Performance\nflops_wrapper.flops_wrapper.FlopsWrapper_input_syntin_Optimization_Control=flops_wrapper.flops_wrapper:FlopsWrapper_input_syntin_Optimization_Control\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Flap_Noise=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Flap_Noise\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_Other=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_Other\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Geometry_BWB=flops_wrapper.flops_wrapper:FlopsWrapper_output_Geometry_BWB\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Engine=flops_wrapper.flops_wrapper:FlopsWrapper_output_Engine\nflops_wrapper.flops_wrapper.FlopsWrapper_input_asclin=flops_wrapper.flops_wrapper:FlopsWrapper_input_asclin\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Weight_Inertia=flops_wrapper.flops_wrapper:FlopsWrapper_output_Weight_Inertia\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Engine_Parameters=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Engine_Parameters\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Fuel_System=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Fuel_System\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Ground_Operations=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Ground_Operations\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Payload=flops_wrapper.flops_wrapper:FlopsWrapper_output_Payload\nflops_wrapper.flops_wrapper.FlopsWrapper_input_fusein_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_fusein_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_output=flops_wrapper.flops_wrapper:FlopsWrapper_output\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Weight_Wing=flops_wrapper.flops_wrapper:FlopsWrapper_output_Weight_Wing\nflops_wrapper.flops_wrapper.FlopsWrapper_input_aerin_Takeoff_Landing=flops_wrapper.flops_wrapper:FlopsWrapper_input_aerin_Takeoff_Landing\nflops_wrapper.flops_wrapper.FlopsWrapper_input=flops_wrapper.flops_wrapper:FlopsWrapper_input\nflops_wrapper.flops_wrapper.FlopsWrapper_input_fusein=flops_wrapper.flops_wrapper:FlopsWrapper_input_fusein\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engdin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_engdin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engdin=flops_wrapper.flops_wrapper:FlopsWrapper_input_engdin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin_Integration_Intervals=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin_Integration_Intervals\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Fan=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Fan\nflops_wrapper.flops_wrapper.FlopsWrapper_input_aerin=flops_wrapper.flops_wrapper:FlopsWrapper_input_aerin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_Engine_Weight=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_Engine_Weight\nflops_wrapper.flops_wrapper.FlopsWrapper_input_costin_Mission_Performance=flops_wrapper.flops_wrapper:FlopsWrapper_input_costin_Mission_Performance\nflops_wrapper.flops_wrapper.FlopsWrapper_input_syntin_Variables=flops_wrapper.flops_wrapper:FlopsWrapper_input_syntin_Variables\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Override=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Override\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Crew_Payload=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Crew_Payload\nflops_wrapper.flops_wrapper.FlopsWrapper_input_mission_definition=flops_wrapper.flops_wrapper:FlopsWrapper_input_mission_definition\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_deck=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_deck\nflops_wrapper.flops_wrapper.FlopsWrapper_input_proin=flops_wrapper.flops_wrapper:FlopsWrapper_input_proin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Jet=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Jet\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_User_Weights=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_User_Weights\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_confin_Objective=flops_wrapper.flops_wrapper:FlopsWrapper_input_confin_Objective\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Propeller=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Propeller\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engdin_Special_Options=flops_wrapper.flops_wrapper:FlopsWrapper_input_engdin_Special_Options\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Tails_Fins=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Tails_Fins\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_Noise_Data=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_Noise_Data\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Propulsion=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Propulsion\nflops_wrapper.flops_wrapper.FlopsWrapper=flops_wrapper.flops_wrapper:FlopsWrapper\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Landing_Gear=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Landing_Gear\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Turn_Segments=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Turn_Segments\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Turbine=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Turbine\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Descent=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Descent\nflops_wrapper.flops_wrapper.FlopsWrapper_input_engine_IC_Engine=flops_wrapper.flops_wrapper:FlopsWrapper_input_engine_IC_Engine\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Climb=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Climb\nflops_wrapper.flops_wrapper.FlopsWrapper_input_confin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_confin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Airframe=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Airframe\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Observers=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Observers\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Performance_Segments=flops_wrapper.flops_wrapper:FlopsWrapper_output_Performance_Segments\nflops_wrapper.flops_wrapper.FlopsWrapper_input_wtin_Wing_Data=flops_wrapper.flops_wrapper:FlopsWrapper_input_wtin_Wing_Data\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Noise=flops_wrapper.flops_wrapper:FlopsWrapper_output_Noise\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Weight=flops_wrapper.flops_wrapper:FlopsWrapper_output_Weight\nflops_wrapper.flops_wrapper.FlopsWrapper_output_Geometry=flops_wrapper.flops_wrapper:FlopsWrapper_output_Geometry\nflops_wrapper.flops_wrapper.FlopsWrapper_input_fusein_BWB=flops_wrapper.flops_wrapper:FlopsWrapper_input_fusein_BWB\nflops_wrapper.flops_wrapper.FlopsWrapper_input_noisin_Core=flops_wrapper.flops_wrapper:FlopsWrapper_input_noisin_Core\nflops_wrapper.flops_wrapper.FlopsWrapper_input_nacell=flops_wrapper.flops_wrapper:FlopsWrapper_input_nacell\nflops_wrapper.flops_wrapper.FlopsWrapper_input_aerin_Basic=flops_wrapper.flops_wrapper:FlopsWrapper_input_aerin_Basic\nflops_wrapper.flops_wrapper.FlopsWrapper_input_option_Excess_Power_Plot=flops_wrapper.flops_wrapper:FlopsWrapper_input_option_Excess_Power_Plot\nflops_wrapper.flops_wrapper.FlopsWrapper_input_missin_Reserve=flops_wrapper.flops_wrapper:FlopsWrapper_input_missin_Reserve\nflops_wrapper.flops_wrapper.FlopsWrapper_input_tolin_Landing=flops_wrapper.flops_wrapper:FlopsWrapper_input_tolin_Landing\nflops_wrapper.flops_wrapper.FlopsWrapper_input_aero_data=flops_wrapper.flops_wrapper:FlopsWrapper_input_aero_data\nflops_wrapper.flops_wrapper.FlopsWrapper_input_costin_Cost_Technology=flops_wrapper.flops_wrapper:FlopsWrapper_input_costin_Cost_Technology',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth T. Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'flops_wrapper',
 'package_data': {'flops_wrapper': []},
 'package_dir': {'': 'src'},
 'packages': ['flops_wrapper'],
 'url': 'https://github.com/OpenMDAO-Plugins/flops_wrapper',
 'version': '0.10',
 'zip_safe': False}


setup(**kwargs)

