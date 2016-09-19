.. _fwflag_from_file:
===========
--from_file
===========
Switch
======

--from_file FILENAME

Description
===========

Text file where fwInterface flags can be set. See also: --to_file

Argument and Default Value
==========================

No defaults

Details
=======

Any variable in the text file can be overridden by the command line. Precedence: command line > init file > default. Do NOT quote strings. Lists must be comma separated. 

This is a list of all of the variables that can be read from the file:

 [constants] 
 corpdb = 
 corptable = 
 correl_field = 
 mysql_host = 
 message_field = 
 messageid_field = 
 date_field = 
 lexicondb = 
 feattable = 
 featnames = 
 featlabelmaptable = 
 featlabelmaplex = 
 lextable = 
 wordTable = 
 outcometable = 
 outcomefields = 
 outcomecontrols = 
 outcomeinteraction = 
 groupfreqthresh = 
 outputname = 
 p_correction_method = 
 tagcloudcolorscheme = 
 maxP = 
 encoding = 
Note: when using an init file outside of fwInterface, i.e., when using the classes explicitly, most of these values will be ignored. 


Other Switches
==============


Example Commands
================
.. code:doc:`fwflag_block`:: python


Give the init file myInit.txt:
 [constants] 
 corpdb = county_addiction
 corptable = msgs_2011to13
 correl_field = cnty
 feattable = feat$cat_met_a30_2000_cp_w$msgs_2011to13$cnty$16to16
 outcome_table = main_interest_vars_controls
 outcome_value_fields = ExcessDrink_Percent, AlcDrivingDeaths_Percent
 outcome_controls = age_lt1, age_1to4
 wordTable = feat$1gram$msgs_2011to13$cnty$16to16$0_1
 output_name = /home/sgiorgi/xxx_output
 maxP = 0.05
 p_correction_method = bonferroni
 groupfreqthresh = 40000
the command
 ./fwInterface.py :doc:`fwflag_from_file` myInit.txt  :doc:`fwflag_correlate` 
is equivalent to:

  ./fwInterface.py :doc:`fwflag_d` county_addiction :doc:`fwflag_t` msgs_2011to13 :doc:`fwflag_c` cnty :doc:`fwflag_word_table` \ 
  'feat$1gram$msgs_2011to13$cnty$16to16$0_1' :doc:`fwflag_group_freq_thresh` 40000 \ 
 :doc:`fwflag_f` 'feat$cat_met_a30_2000_cp_w$msgs_2011to13$cnty$16to16' :doc:`fwflag_outcome_table` main_interest_vars_controls \ 
 :doc:`fwflag_outcomes` ExcessDrink_Percent AlcDrivingDeaths_Percent :doc:`fwflag_controls` age_lt1 age_1to4 :doc:`fwflag_correlate`  \ 
 :doc:`fwflag_output_name` ~/xxx_output :doc:`fwflag_p_value` 0.05 :doc:`fwflag_p_correction` 'bonferroni'