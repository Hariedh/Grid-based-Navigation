# Grid-based-Navigation
Author : Hariedh Raju

# Grid-Based Navigation Problem Solvers

This repository contains Python programs for solving the grid-based navigation problem, where the objective is to find the shortest path from a start cell to a goal cell in a grid while avoiding obstacles. It provides implementations for solving the problem using various techniques, including search algorithms and random walk.

## Problem Description

The grid-based navigation problem involves a grid of cells, each of which can be either empty ("E") or blocked ("X"). The goal is to find the shortest path from a start cell to a goal cell while avoiding obstacles. Movement is allowed only horizontally or vertically (no diagonal moves).

## Programs

### 1. A* Search Algorithm

The program `with algo.py` implements the A* search algorithm to find the shortest path from a start cell to a goal cell. This algorithm takes into account both the cost to reach the current cell and a heuristic function (Manhattan distance) to estimate the cost from the current cell to the goal. It uses a priority queue to explore cells with lower estimated costs first.

### 2. Random Grid Generator and Random Walk

The program `without algo.py` generates a random grid with a specified size and obstacle probability. It then uses a random walk algorithm to explore the grid from a start cell to a goal cell. The random walk algorithm generates random moves (up, down, left, right) to navigate the grid.

## Usage

Each program can be run separately to solve grid-based navigation problems


