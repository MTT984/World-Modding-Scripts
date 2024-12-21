## Collection of Python Scripts for NFS World Modding

This is a collection of Python scripts designed for creating mods for **NFS World**.

These scripts are used internally by a *small secret group* :lostwoo: from Spark. The main goal was to speed up modding creation, organize our workflow, and simplify/reduce some repetitive tasks.

*that's why the quality of these scripts might be a bit questionable, with low modularity, no good standards... or any other shi... but yea they get the job done, hope it works for you too!*

### **Scripts:**
---
#### **> customCarParts**
Generates files for use in **GlobalC**.

- **PresetsSkins**
- **CarParts**
  - **expanded**: Includes hood/spoiler parts, plus STYLE15.
  - **vanilla**: Standard game parts (except SPOILERS).
  - **reduced_1**: Support for reduced parts.
  - **reduced_2**: Support for even more reduced parts.
---
#### **> icon_gen (outdated)**
Used to generate vinyl icons/thumbnails, styled to match the NFS World aesthetic (bluish tone).

---

#### **> visualparts_script (obsolete, replaced by world_vps)**
Generates .nfsms and .xml files related to custom parts (like HOOD, SPOILER, etc.).

---

#### **> world_blender_ctk**
Used within **Blender** to speed up car model creation.

- Renames car model meshes when needed (important for exporting the model).
- Returns the rotation value of the license plate.
- Creates a temporary base file to be adapted into the **CarToolKit Configuration File**. This file includes values for **PARTS**, **MATERIALS**, and **MARKERS** (VERY IMPORTANT AND USEFUL FOR EXPORTING MODELS).

---

#### **> world_vps**
An improved version of **visualparts_script**, now with an interface and better modularity to support additional parts (like **FRONT_TIRE**, **MIRRORS**, **KIT**, etc.).

*Some improvements to be made.*
