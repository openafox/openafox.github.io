---
layout: post
title: Atomic Force Microscopy Tips and Tricks
tag:
  - AFM
  - Scihacks
  - Manuals
category: Science

excerpt: Some tips and tricks to help with AC (Tapping) mode on an Asylum MFP-3D AFM.
---

Some tips and tricks to help with AC (Tapping) mode on an Asylum MFP-3D AFM.

[Printable Version](https://docs.google.com/document/d/1eofNETKpSAIRUujjaL2GFZ-a_owEZ6GsJn_wqCc70Vg/export?format=pdf)

# Quick guide to how AC mode works

Shown here are the effects of changing parameters or moving over a sample feature.  This is under normal running conditions with no adjustments to the head height.
![How AFM AC mode works](/resources/img/afm-operation.png)

**Voltage** - measured oscillation (vibration) of the tip.

**Z-Voltage (ZV)** - voltage applied to the piezo adjusting tip height,↑V = away from sample.

**Drive Frequency (DF)**- tip oscillation frequency.

**Set Point (SP)** - Voltage maintained by adjusting the z-voltage (surface force)
: (damping the oscillation). ↓ Set Point ↑ Force on surface

**Drive amplitude (DA)** - is the voltage applied to oscillate the tip.
: Works opposite of Set point.  ↑ Drive Amp ↑ Force on surface

**Gain** - response time of the z-voltage.   Too high = ringing and too low = no trace.

**Phase** - the difference between the input and output signals.

# Save Time - Make an experiment file (.pxp)...

It saves your workspace, settings, and save location (yes, you can change it!)

Don’t select a mode on start up; just open your experiment file...

# Tuning Parameters

| Repulsive mode | Attractive mode |
|:---------------|:----------------|
| Closer to surface (~1Å) - sharper images - faster tip/sample wear | For ‘Soft’ Samples - often dominated by static charges |
| Use Higher Free Air Amp (1V) | Use Lower Free Air Amp (0.3V) |
| Image at < ‘free air’ phase | Image at > ‘free air’ phase |
| Low Q | High Q |
| Smaller tip radius (shap tip needed) | Larger tip radius |
| Set $$f$$ -8% $$f_o$$ (left of Resonance) | Set $$f$$ +10% $$f_o$$ (right of Resonance) |

![AFM Tuning](/resources/img/afm-tuning.svg){: style='width:50%'}
![AFM Tip Distance](/resources/img/afm-tip-distance.png){: style='width:50%'}
Form [NPTEL courses](http://nptel.ac.in/courses/102103044/module3/lec19/4.html){: target="_blank"}

# Max Band Width (Max Scan Rate)

Sample Speed must be < Collection Limit to achieve quality scans.
$$Collection\: Limit[khz]=\frac{Resonance\: Frequency}{Quality}$$
$$Sample\: Speed[khz]=(Points\&Lines \times 1.25 \times 2) \times Scan\: Rate$$

If not:
: Add increments of -0.005 to the Qgain
: Then “One Tune” – Recalc CL

# Phase Hopping (red-blue...)

**Or tip not tracing well**

Increasing the DA may help (doubling will often stabilize the phase):
: Just jump up the DA or;
: Save the tip by; Withdrawing the tip → doing the increase → Re-engage - Try up to 4x

Gain will need to be decreased to account for increase in DA

# Mounting Your Sample

Reduces drift - Fewer but better contacts - Lower chance of air bubbles - Makes removal easier
![AFM Sample Mounting](/resources/img/afm-mount.png)

# Imaging Panels

**Height** - Corrected Z-piezo voltage (tip height found by feedback loop) - true surface height data

**Phase** - Phase lag between the drive signal and the detected signal

**Z-Sensor** - Linear detector of Z height much more accurate than height for features above 1μm but not as good below

**Amplitude** - Deflection or angle of the tip (not real height of surface)

# Finding the Laser

Center LDX and Y (8 “turns” from ends)

Laser will be on tip within 1 turn

Turn =
:Finger on side opposite of rotation direction
:Rotate until finger hits other side ≈180°

# Deflection

As Shown turn the PD nob:
:Toward the back of the head to make the deflection more negative
:Toward the front to make more positive
**DO NOT EVER** force the PD nob - it can cause **serious damage**!
![AFM Head](/resources/img/afm-head.png){: width="50%"}
![AFM Deflection](/resources/img/afm-deflection.png)

# Save your tip!!!

**Load It Properly and Let It Equilibrate!!**

1. Load tip as shown to the below ![AFM Tip Loading](/resources/img/afm-tip2.png){: width="50%"}
2. Load sample and place head (take care not to crash tip!)
3. Align laser spot toward end of cantilever and zero deflection ![AFM Tip Laser](/resources/img/afm-tip.png) ![AFM Sum and Deflection Meter](/resources/img/afm-meter.png){: width="50%"}
4. Do “Auto Tune”, -8% fo
  * Check achievable scan rate
5. Let sit for 10+ mins (equilibrate)
6. Re-zero Deflection
7. Do “Auto Tune”, -8% fo
  * Check achievable scan rate
8. Soft Engage


# Save your tip!!! - Soft Engage!

1. Perform an Auto Tune
2. Set the Set Point voltage to 950 mV
3. Click ‘Engage’ button
4. Slowly turn the front thumbwheel CCW (Lowering the head)
  * Monitor the amplitude voltage (S&D meter)
  * Wait for it to equal the Set Point voltage
    * This is a false engagement (Engaging water layer…)
  * Lower the head until ZV is about 40V (halfway blue)
    * You’ll notice the ZV seems to float/drift as you move the thumbwheel- that’s because it’s falsely engaged!
5. With the radio button for the Set Point voltage activated use the ‘Hamster’ wheel on front of controller to increase the force
  * The ZV will move to some more positive voltage value (more red)
  * At some point you’ll notice the ZV will no longer quickly become more positive (It may still slowly get more positive)
6. At this point, the tip is ‘hard’ engaged on the surface
7. Using the thumb wheel adjust the ZV to ≈50V to achieve 70V after reengage
8. Withdraw or increase set point to pop tip of surface and lower door

# Save your tip!!! - Adjust Gain!

* Increase until you see ringing
* Decrease to get ringing to go away
* Saves tip by optimizing the gain, minimizing the chance that the tip will crash into a large feature

# Tip Motion

Tip can be moved from -40 μm to +40 μm or do an 80 μm scan max

![AFM tip motion direction](/resources/img/afm-motion.png)
