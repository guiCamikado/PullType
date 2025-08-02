# Modules

This is where the system that Creates, manages and delete the "Modules System" is storaged.

# Profile Editing System Design

There are two ways to think about this:

## 1. Editable Blocks (like Steam)
- Gives users more personality and creative freedom.
- More fun and personal.

## 2. Standardized Layout (like Instagram)
- Safer and more commonly used.
- Feels more professional, but takes away the fun of building a “personal profile”.

---

## Concept

When someone edits their profile, they will be able to use **Modules**.

Each module will have a **type**, functioning like a widget (e.g., **image bank**, **text box**, etc.), following a **guide-based design** approach.

---

## Rules and Behavior

- ✅ **Modules are unlimited**.
- ❌ **It is impossible to create a new module if a parent module contains a child module with no items inside**.
- ⚠️ A module named **`ROOT`** is automatically created by
