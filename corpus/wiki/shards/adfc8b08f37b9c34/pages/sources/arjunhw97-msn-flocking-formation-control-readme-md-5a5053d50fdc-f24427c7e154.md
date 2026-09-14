---
access: public
aliases: []
claim_ids:
- clm_096ac87fd6ba05a5437b26d04b4be8b3084590d2de1643424f6a772183c4173e
- clm_374262ad54f8b1dda9038030e29d0f4f8d6c86e28eccfddf375bd63be4717ac1
- clm_39682cecd7fbf136066441c144cd88a7885bc9769ca2880a8bef289ec621583b
- clm_4cdaca73b6464be46b4b7e47b1673c112b90974e3ff9ffb4e868703cf48e2173
- clm_55254b88a43fea98d4f5ec14099b8d5859c02c1e9ea242d28aba8e8b9aaf610e
- clm_67fb9a84f1c33b987dd8d3bfe31727dc0a93423b0b802c7e646fb484fa0f7d31
- clm_76b65866cfb58ea91a44cf0a5659d20b52d684e0e992445cbdf0ee450167b9ef
- clm_7bf29c44eec774586f160ef37b612564cbc45bd7ca8a921fb6182fe0ee836c1b
- clm_7e29e9a69ee470133f85bdeb9ad0a0b1807d34ec2269fbf58dc650f932bf52b1
- clm_9523ab7623bc22587094a9061d33898d4d48dca72cf06ed0e642edf3e6f64389
- clm_c0abbf135c83887dc31ab5f8503f72ace13f868bf3da795b348c01970dd41108
maturity: draft
page_id: pg_185d8419c58353b8b33ff24427c7e154
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1ad1d2d7dbfe5a44ac486dc005bfd75a
title: arjunhw97/MSN-Flocking-Formation-Control/README.md @ 5a5053d50fdc
updated_at: '2026-09-14T03:36:00Z'
---

# arjunhw97/MSN-Flocking-Formation-Control/README.md @ 5a5053d50fdc

<!-- rcw:begin owner=source:src_1ad1d2d7dbfe5a44ac486dc005bfd75a block=evidence -->
- Case 2 (MSN2.m) implements quasi-lattice flocking toward a static gamma-agent target at coordinates (150, 150). [@claim:clm_096ac87fd6ba05a5437b26d04b4be8b3084590d2de1643424f6a772183c4173e]
- The project is based on a published flocking control paper, which the README links via CiteSeerX and recommends reading before the code. [@claim:clm_374262ad54f8b1dda9038030e29d0f4f8d6c86e28eccfddf375bd63be4717ac1]
- Case 5 (MSN5.m) adds obstacle avoidance: a circular obstacle of radius 15 centered at (100, 25) with the target at (200, 25). [@claim:clm_39682cecd7fbf136066441c144cd88a7885bc9769ca2880a8bef289ec621583b]
- Algorithm equations are presented only as embedded images (alg1.JPG, alg2.JPG, alg21.JPG, alg3.JPG, etc.) in the README rather than as text, suggesting the math is documented visually per case. [@claim:clm_4cdaca73b6464be46b4b7e47b1673c112b90974e3ff9ffb4e868703cf48e2173]
- The repository provides five MATLAB scripts, MSN1.m through MSN5.m, corresponding to five simulation cases described in the README. [@claim:clm_55254b88a43fea98d4f5ec14099b8d5859c02c1e9ea242d28aba8e8b9aaf610e]
- Repository development practice: the README instructs users to install the latest MATLAB, copy the 'source code' directory into their MATLAB directory, and run any of MSN1.m through MSN5.m directly. [@claim:clm_67fb9a84f1c33b987dd8d3bfe31727dc0a93423b0b802c7e646fb484fa0f7d31]
- Each case produces MATLAB plots including node flocking/fragmentation, velocity, connectivity, and trajectory; dynamic-target cases also plot center of mass and target trajectory. [@claim:clm_76b65866cfb58ea91a44cf0a5659d20b52d684e0e992445cbdf0ee450167b9ef]
- Case 3 (MSN3.m) uses a 150x150 area with a gamma agent following a sine wave trajectory, and Case 4 (MSN4.m) uses a circular trajectory target. [@claim:clm_7bf29c44eec774586f160ef37b612564cbc45bd7ca8a921fb6182fe0ee836c1b]
- Epsilon is set to 0.1 and Delta_t to 0.009; the README notes these two parameters are optional and can be changed by the user. [@claim:clm_7e29e9a69ee470133f85bdeb9ad0a0b1807d34ec2269fbf58dc650f932bf52b1]
- Case 1 (MSN1.m) simulates MSN fragmentation: it generates a connected 100-node network in a 50x50 area, plots the initial deployment, and links neighboring nodes with lines. [@claim:clm_9523ab7623bc22587094a9061d33898d4d48dca72cf06ed0e642edf3e6f64389]
- Simulations use 100 sensor nodes in 2 dimensions with a desired inter-node distance of 15 and interaction range r = k*d where k = 1.2. [@claim:clm_c0abbf135c83887dc31ab5f8503f72ace13f868bf3da795b348c01970dd41108]
<!-- rcw:end owner=source:src_1ad1d2d7dbfe5a44ac486dc005bfd75a block=evidence -->

## Researcher notes

