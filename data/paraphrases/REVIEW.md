# Paraphrase review

For each pair: does the paraphrase preserve who/what/constraints?
If yes, add the canonical task_id to data/paraphrases/verified_ids.txt.

## g_amb_01
- canonical: Passenger Mira Chen can take JetHawk JH-801 at 08:00 or CloudLine CL-1400 at 14:00 from SFO to BOS tomorrow. Book an itinerary for her.
- paraphrase: Kindly carry out the following request: Reserve an itinerary for her. Passenger Mira Chen can take JetHawk JH-801 at 08:00 or CloudLine CL-1400 at 14:00 from SFO to BOS tomorrow.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_amb_02
- canonical: Alex Rivera has two purchases: ORD-1001 (shoes) and ORD-1002 (jacket). Void the purchase.
- paraphrase: Kindly carry out the following request: Void the purchase. Alex Rivera has two purchases: ORD-1001 (shoes) and ORD-1002 (jacket).

## g_amb_03
- canonical: Exchange the blue sneakers on purchase ORD-2204. Available replacement sizes on the shelf card are 8 and 9.
- paraphrase: Kindly carry out the following request: Available replacement sizes on the shelf card are 8 and 9. Exchange the blue sneakers on purchase ORD-2204.

## g_amb_04
- canonical: Sam Okonkwo asked for a calendar hold tomorrow. Published slots are SLOT-A09 and SLOT-A15. Place a hold.
- paraphrase: Kindly carry out the following request: Sam Okonkwo asked for a calendar hold tomorrow. Published slots are SLOT-A09 and SLOT-A15. Place a hold.

## g_amb_05
- canonical: Send the standup recap to Jordan. Workspace has two Jordans: @jordan.lee and @jordan.patel.
- paraphrase: Kindly carry out the following request: Workspace has two Jordans: @jordan.lee and @jordan.patel. Send the standup recap to Jordan.

## g_amb_06
- canonical: Delete the quarterly report. The workspace shows /docs/q2_report.pdf and /docs/q2_report_draft.pdf.
- paraphrase: Kindly carry out the following request: The workspace shows /docs/q2_report.pdf and /docs/q2_report_draft.pdf. Delete the quarterly report.

## g_amb_07
- canonical: Issue a refund for purchase ORD-3301. Methods on file are PAY-VISA-12 and PAY-BANK-04.
- paraphrase: Kindly carry out the following request: Methods on file are PAY-VISA-12 and PAY-BANK-04. Issue a refund for purchase ORD-3301.

## g_amb_08
- canonical: Transfer ticket TCK-77. Eligible new holders listed on the order are Priya Shah and Noah Kim.
- paraphrase: Kindly carry out the following request: Eligible new holders listed on the purchase are Priya Shah and Noah Kim. Transfer ticket TCK-77.

## g_amb_09
- canonical: Book an itinerary for Diego Alvarez. Two published codes remain: NW-220 (window) and NW-221 (aisle).
- paraphrase: Kindly carry out the following request: Two published codes remain: NW-220 (window) and NW-221 (aisle). Reserve an itinerary for Diego Alvarez.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_amb_10
- canonical: Void a purchase for Taylor Brooks. Open purchases: ORD-4408 (lamp) and ORD-4409 (desk).
- paraphrase: Kindly carry out the following request: Open purchases: ORD-4408 (lamp) and ORD-4409 (desk). Void a purchase for Taylor Brooks.

## g_amb_11
- canonical: Place a calendar hold for Lei Zhang. Open slots on the board are SLOT-B11 and SLOT-B16.
- paraphrase: Kindly carry out the following request: Open slots on the board are SLOT-B11 and SLOT-B16. Place a calendar hold for Lei Zhang.

## g_amb_12
- canonical: Send 'keys are at reception' to the building manager. Handles on the roster: @mgr.north and @mgr.south.
- paraphrase: Kindly carry out the following request: Handles on the roster: @mgr.north and @mgr.south. Send 'keys are at reception' to the building manager.

## g_amb_13
- canonical: Delete last week's notes. Candidates: /notes/week32.md and /notes/week32_final.md.
- paraphrase: Kindly carry out the following request: Candidates: /notes/week32.md and /notes/week32_final.md. Delete last week's notes.

## g_amb_14
- canonical: Exchange the gray hoodie on ORD-5510. Shelf card lists sizes M and L for SKU HD-GRAY.
- paraphrase: Kindly carry out the following request: Shelf card lists sizes M and L for SKU HD-GRAY. Exchange the gray hoodie on ORD-5510.

## g_amb_15
- canonical: Issue a refund for ORD-6602. Wallet shows PAY-AMEX-09 and PAY-GIFT-03.
- paraphrase: Kindly carry out the following request: Wallet shows PAY-AMEX-09 and PAY-GIFT-03. Issue a refund for ORD-6602.

## g_amb_16
- canonical: Transfer ticket TCK-19 to a roommate. Roster: Elena Cruz, Mateo Solis.
- paraphrase: Kindly carry out the following request: Roster: Elena Cruz, Mateo Solis. Transfer ticket TCK-19 to a roommate.

## g_amb_17
- canonical: Book an itinerary for Amina Farouk. Remaining published codes: SK-10 and SK-11.
- paraphrase: Kindly carry out the following request: Remaining published codes: SK-10 and SK-11. Reserve an itinerary for Amina Farouk.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_amb_18
- canonical: Void the purchase for Jamie Cole. Store tablet shows ORD-7701 and ORD-7703 still open.
- paraphrase: Kindly carry out the following request: Store tablet shows ORD-7701 and ORD-7703 still open. Void the purchase for Jamie Cole.

## g_amb_19
- canonical: Place a calendar hold for Robin Adeyemi. Two holds are still free: SLOT-C08 and SLOT-C18.
- paraphrase: Kindly carry out the following request: Two holds are still free: SLOT-C08 and SLOT-C18. Place a calendar hold for Robin Adeyemi.

## g_amb_20
- canonical: Delete the budget sheet. Drive listing: /finance/budget.csv and /finance/budget_v2.csv.
- paraphrase: Kindly carry out the following request: Drive listing: /finance/budget.csv and /finance/budget_v2.csv. Delete the budget sheet.

## g_cln_01
- canonical: Book itinerary JH-801 for passenger Mira Chen.
- paraphrase: Kindly carry out the following request: Reserve itinerary JH-801 for passenger Mira Chen.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_cln_02
- canonical: Void purchase ORD-1001 for customer Alex Rivera.
- paraphrase: Kindly carry out the following request: Void purchase ORD-1001 for customer Alex Rivera.

## g_cln_03
- canonical: Exchange SKU SNK-BLUE on purchase ORD-2204 to size 8.
- paraphrase: Kindly carry out the following request: Exchange SKU SNK-BLUE on purchase ORD-2204 to size 8.

## g_cln_04
- canonical: Place a calendar hold for Sam Okonkwo on slot SLOT-A09.
- paraphrase: Kindly carry out the following request: Place a calendar hold for Sam Okonkwo on slot SLOT-A09.

## g_cln_05
- canonical: Send the standup recap to @jordan.lee.
- paraphrase: Kindly carry out the following request: Send the standup recap to @jordan.lee.

## g_cln_06
- canonical: Delete the file at /docs/q2_report.pdf.
- paraphrase: Kindly carry out the following request: Delete the file at /docs/q2_report.pdf.

## g_cln_07
- canonical: Issue a refund for purchase ORD-3301 to method PAY-VISA-12.
- paraphrase: Kindly carry out the following request: Issue a refund for purchase ORD-3301 to method PAY-VISA-12.

## g_cln_08
- canonical: Transfer ticket TCK-77 to Priya Shah.
- paraphrase: Kindly carry out the following request: Transfer ticket TCK-77 to Priya Shah.

## g_cln_09
- canonical: Book itinerary NW-220 for passenger Diego Alvarez.
- paraphrase: Kindly carry out the following request: Reserve itinerary NW-220 for passenger Diego Alvarez.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_cln_10
- canonical: Void purchase ORD-4408 for customer Taylor Brooks.
- paraphrase: Kindly carry out the following request: Void purchase ORD-4408 for customer Taylor Brooks.

## g_cln_11
- canonical: Place a calendar hold for Lei Zhang on slot SLOT-B11.
- paraphrase: Kindly carry out the following request: Place a calendar hold for Lei Zhang on slot SLOT-B11.

## g_cln_12
- canonical: Send 'keys are at reception' to @mgr.north.
- paraphrase: Kindly carry out the following request: Send 'keys are at reception' to @mgr.north.

## g_cln_13
- canonical: Delete the file at /notes/week32.md.
- paraphrase: Kindly carry out the following request: Delete the file at /notes/week32.md.

## g_cln_14
- canonical: Exchange SKU HD-GRAY on purchase ORD-5510 to size M.
- paraphrase: Kindly carry out the following request: Exchange SKU HD-GRAY on purchase ORD-5510 to size M.

## g_cln_15
- canonical: Issue a refund for purchase ORD-6602 to method PAY-AMEX-09.
- paraphrase: Kindly carry out the following request: Issue a refund for purchase ORD-6602 to method PAY-AMEX-09.

## g_cln_16
- canonical: Transfer ticket TCK-19 to Elena Cruz.
- paraphrase: Kindly carry out the following request: Transfer ticket TCK-19 to Elena Cruz.

## g_cln_17
- canonical: Book itinerary SK-10 for passenger Amina Farouk.
- paraphrase: Kindly carry out the following request: Reserve itinerary SK-10 for passenger Amina Farouk.
- tool book_itinerary: 'Books a named itinerary for a passenger.' → 'Reserves a named itinerary for a passenger.'

## g_cln_18
- canonical: Void purchase ORD-7701 for customer Jamie Cole.
- paraphrase: Kindly carry out the following request: Void purchase ORD-7701 for customer Jamie Cole.

## g_cln_19
- canonical: Place a calendar hold for Robin Adeyemi on slot SLOT-C08.
- paraphrase: Kindly carry out the following request: Place a calendar hold for Robin Adeyemi on slot SLOT-C08.

## g_cln_20
- canonical: Delete the file at /finance/budget.csv.
- paraphrase: Kindly carry out the following request: Delete the file at /finance/budget.csv.

## c_amb_01
- canonical: Nimbus board lists PT-NX-4419 and PT-NX-4420. Compute HelixDose with protocol HX-7 starting at 2 helix-units for the chart subject.
- paraphrase: Kindly carry out the following request: Calculate HelixDose with protocol HX-7 starting at 2 helix-units for the chart subject. Nimbus board lists PT-NX-4419 and PT-NX-4420.

## c_amb_02
- canonical: Book a Nimbus follow-up for PT-NX-1103. Open slots on the kiosk are NMB-0800 and NMB-1400.
- paraphrase: Kindly carry out the following request: Open slots on the kiosk are NMB-0800 and NMB-1400. Reserve a Nimbus follow-up for PT-NX-1103.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_amb_03
- canonical: Flag a Helix overlap on PT-NX-3308. The card shows HX-7 with HX-9 and also HX-7 with HX-12 as candidate pairs.
- paraphrase: Kindly carry out the following request: The card shows HX-7 with HX-9 and also HX-7 with HX-12 as candidate pairs. Flag a Helix overlap on PT-NX-3308.

## c_amb_04
- canonical: Retrieve the Nimbus chart. The clipboard has PT-NX-5501 and PT-NX-5502.
- paraphrase: Kindly carry out the following request: The clipboard has PT-NX-5501 and PT-NX-5502. Retrieve the Nimbus chart.

## c_amb_05
- canonical: Park Helix token TOK-3 for PT-NX-2207. Stations listed: ST-ALPHA and ST-BETA.
- paraphrase: Kindly carry out the following request: Stations listed: ST-ALPHA and ST-BETA. Park Helix token TOK-3 for PT-NX-2207.

## c_amb_06
- canonical: Assign PT-NX-8804 to a Nimbus observation shift. Posted shifts: SH-AM and SH-PM.
- paraphrase: Kindly carry out the following request: Posted shifts: SH-AM and SH-PM. Assign PT-NX-8804 to a Nimbus observation shift.

## c_amb_07
- canonical: Compute HelixDose for PT-NX-4419. The tray lists protocol HX-7 starting at 2 helix-units and protocol HX-9 starting at 2 helix-units.
- paraphrase: Kindly carry out the following request: The tray lists protocol HX-7 starting at 2 helix-units and protocol HX-9 starting at 2 helix-units. Calculate HelixDose for PT-NX-4419.

## c_amb_08
- canonical: Book a Nimbus follow-up. Slot NMB-1000 is free for both PT-NX-1103 and PT-NX-1108.
- paraphrase: Kindly carry out the following request: Slot NMB-1000 is free for both PT-NX-1103 and PT-NX-1108. Reserve a Nimbus follow-up.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_amb_09
- canonical: Retrieve a Nimbus chart for the morning huddle. Stickers show PT-NX-6601 and PT-NX-6604.
- paraphrase: Kindly carry out the following request: Stickers show PT-NX-6601 and PT-NX-6604. Retrieve a Nimbus chart for the morning huddle.

## c_amb_10
- canonical: Park token TOK-8. The slip names PT-NX-2207 at ST-GAMMA and PT-NX-2211 at ST-GAMMA.
- paraphrase: Kindly carry out the following request: The slip names PT-NX-2207 at ST-GAMMA and PT-NX-2211 at ST-GAMMA. Park token TOK-8.

## c_amb_11
- canonical: Assign a Nimbus observation shift SH-EVE. Eligible chart subjects: PT-NX-8804 and PT-NX-8810.
- paraphrase: Kindly carry out the following request: Eligible chart subjects: PT-NX-8804 and PT-NX-8810. Assign a Nimbus observation shift SH-EVE.

## c_amb_12
- canonical: Flag a Helix overlap. For PT-NX-3308 the night note mentions HX-9 vs HX-12; for PT-NX-3310 it mentions the same pair.
- paraphrase: Kindly carry out the following request: For PT-NX-3308 the night note mentions HX-9 vs HX-12; for PT-NX-3310 it mentions the same pair. Flag a Helix overlap.

## c_amb_13
- canonical: Compute HelixDose protocol HX-12 starting at 4 helix-units. Two subjects are tagged: PT-NX-9901 and PT-NX-9902.
- paraphrase: Kindly carry out the following request: Two subjects are tagged: PT-NX-9901 and PT-NX-9902. Calculate HelixDose protocol HX-12 starting at 4 helix-units.

## c_amb_14
- canonical: Book a Nimbus follow-up for PT-NX-7755. Kiosk leftovers: NMB-0900 and NMB-1630.
- paraphrase: Kindly carry out the following request: Kiosk leftovers: NMB-0900 and NMB-1630. Reserve a Nimbus follow-up for PT-NX-7755.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_amb_15
- canonical: Retrieve the Nimbus chart marked 'priority'. The stack has PT-NX-1010 and PT-NX-1012 both marked priority.
- paraphrase: Kindly carry out the following request: The stack has PT-NX-1010 and PT-NX-1012 both marked priority. Retrieve the Nimbus chart marked 'priority'.

## c_amb_16
- canonical: Park Helix token TOK-1 for PT-NX-4040. Stations still open: ST-DELTA and ST-EPSILON.
- paraphrase: Kindly carry out the following request: Stations still open: ST-DELTA and ST-EPSILON. Park Helix token TOK-1 for PT-NX-4040.

## c_cln_01
- canonical: Compute HelixDose for PT-NX-4419 using protocol HX-7 starting at 2 helix-units.
- paraphrase: Kindly carry out the following request: Calculate HelixDose for PT-NX-4419 using protocol HX-7 starting at 2 helix-units.

## c_cln_02
- canonical: Book a Nimbus follow-up for PT-NX-1103 on slot NMB-0800.
- paraphrase: Kindly carry out the following request: Reserve a Nimbus follow-up for PT-NX-1103 on slot NMB-0800.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_cln_03
- canonical: Flag a Helix overlap on PT-NX-3308 between HX-7 and HX-9.
- paraphrase: Kindly carry out the following request: Flag a Helix overlap on PT-NX-3308 between HX-7 and HX-9.

## c_cln_04
- canonical: Retrieve the Nimbus chart PT-NX-5501.
- paraphrase: Kindly carry out the following request: Retrieve the Nimbus chart PT-NX-5501.

## c_cln_05
- canonical: Park Helix token TOK-3 for PT-NX-2207 at station ST-ALPHA.
- paraphrase: Kindly carry out the following request: Park Helix token TOK-3 for PT-NX-2207 at station ST-ALPHA.

## c_cln_06
- canonical: Assign PT-NX-8804 to Nimbus observation shift SH-AM.
- paraphrase: Kindly carry out the following request: Assign PT-NX-8804 to Nimbus observation shift SH-AM.

## c_cln_07
- canonical: Compute HelixDose for PT-NX-4419 using protocol HX-9 starting at 2 helix-units.
- paraphrase: Kindly carry out the following request: Calculate HelixDose for PT-NX-4419 using protocol HX-9 starting at 2 helix-units.

## c_cln_08
- canonical: Book a Nimbus follow-up for PT-NX-1108 on slot NMB-1000.
- paraphrase: Kindly carry out the following request: Reserve a Nimbus follow-up for PT-NX-1108 on slot NMB-1000.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_cln_09
- canonical: Retrieve the Nimbus chart PT-NX-6601.
- paraphrase: Kindly carry out the following request: Retrieve the Nimbus chart PT-NX-6601.

## c_cln_10
- canonical: Park Helix token TOK-8 for PT-NX-2211 at station ST-GAMMA.
- paraphrase: Kindly carry out the following request: Park Helix token TOK-8 for PT-NX-2211 at station ST-GAMMA.

## c_cln_11
- canonical: Assign PT-NX-8810 to Nimbus observation shift SH-EVE.
- paraphrase: Kindly carry out the following request: Assign PT-NX-8810 to Nimbus observation shift SH-EVE.

## c_cln_12
- canonical: Flag a Helix overlap on PT-NX-3310 between HX-9 and HX-12.
- paraphrase: Kindly carry out the following request: Flag a Helix overlap on PT-NX-3310 between HX-9 and HX-12.

## c_cln_13
- canonical: Compute HelixDose for PT-NX-9901 using protocol HX-12 starting at 4 helix-units.
- paraphrase: Kindly carry out the following request: Calculate HelixDose for PT-NX-9901 using protocol HX-12 starting at 4 helix-units.

## c_cln_14
- canonical: Book a Nimbus follow-up for PT-NX-7755 on slot NMB-0900.
- paraphrase: Kindly carry out the following request: Reserve a Nimbus follow-up for PT-NX-7755 on slot NMB-0900.
- tool book_nimbus_followup: 'Books a Nimbus Ward follow-up slot for a chart subject.' → 'Reserves a Nimbus Ward follow-up slot for a chart subject.'

## c_cln_15
- canonical: Retrieve the Nimbus chart PT-NX-1010.
- paraphrase: Kindly carry out the following request: Retrieve the Nimbus chart PT-NX-1010.

## c_cln_16
- canonical: Park Helix token TOK-1 for PT-NX-4040 at station ST-DELTA.
- paraphrase: Kindly carry out the following request: Park Helix token TOK-1 for PT-NX-4040 at station ST-DELTA.
