# High Card

A simple two-player High Card game built in Python as a small project to practise object-oriented programming (OOP).

## Overview

Players compete over five rounds, drawing one card each round from a shuffled deck. The player with the higher card wins the round and earns one point. The player with the highest score at the end wins.

## Features

- Shuffled deck containing cards numbered 1–10.
- Two-player gameplay.
- Five rounds per game.
- Automatic card drawing and comparison.
- Score tracking and winner determination.
- Draw handling when both players have equal scores.

## OOP Concepts

This project explores several fundamental object-oriented programming concepts:

- **Classes and objects:** Separate classes represent the deck, players and game.
- **Encapsulation:** Each class manages its own data and related behaviour.
- **Composition:** The game contains a deck and two player objects.
- **Object interaction:** Player objects interact with the shared deck to draw cards.

## Technologies

- Python
- `random` (standard library)

## How to Play

1. Run the Python program.
2. Two players are created.
3. The deck is shuffled.
4. Each player draws one card per round.
5. The higher card earns a point.
6. After five rounds, the final scores and winner are displayed.

## Purpose

This project was created as a practical exercise in understanding how classes can organise data and behaviour, and how multiple objects can interact within a program.