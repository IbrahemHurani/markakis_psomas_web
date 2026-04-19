# Markakis-Psomas Fair Allocation Algorithm

A web-based application for implementing and visualizing the **Markakis-Psomas algorithm** for fair allocation of indivisible goods among multiple agents.

## Overview

This project provides an interactive interface for exploring fair division of resources using the algorithm proposed by **Markakis and Psomas** in their 2011 paper: *"On Worst-Case Allocations in the Presence of Indivisible Goods"*.

The algorithm guarantees that each agent receives a bundle worth at least V<sub>n</sub>(α<sub>i</sub>), where α<sub>i</sub> is the proportion of the most valuable item to that agent relative to their total valuation of all items.

## Features

- **Manual Input**: Define custom agents and items with specific valuations
- **Random Generation**: Automatically generate test cases with random valuations
- **Step-by-Step Visualization**: View detailed logs of the allocation algorithm's execution
- **Fair Allocation Results**: See the final allocation and value distribution for each agent
- **Educational Interface**: Clean, intuitive UI designed for learning and experimentation

## How It Works

1. **Input Valuation Matrix**: Specify agents, items, and valuations (manual or random)
2. **Algorithm Execution**: Calculate fairness thresholds for each agent
3. **Incremental Allocation**: Allocate bundles based on fairness guarantees
4. **Result Display**: View allocation results and execution logs

## Algorithm Steps

1. For each agent, compute α<sub>i</sub> = (largest item value) / (total value of all items)
2. Calculate V<sub>n</sub>(α<sub>i</sub>) using the fairness formula from the paper
3. Allocate items incrementally until one agent meets their fairness threshold
4. Assign the bundle to that agent
5. Normalize valuations of remaining agents for remaining items
6. Recursively allocate remaining items to remaining agents

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd markakis_psomas_web-main
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Using the Web Interface

1. **Home Page**: Learn about the algorithm and its guarantees
2. **Manual Input**: 
   - Enter agent names and item names
   - Specify valuations for each (agent, item) pair
   - Submit to see the allocation result
3. **Random Input**:
   - Choose number of agents and items
   - Generate random valuations
   - Preview and run the allocation algorithm

## Project Structure

```
├── app.py                 # Flask application and route handlers
├── algorithm.py          # Core algorithm implementation using fairpyx
├── requirements.txt      # Python dependencies
├── static/
│   ├── style.css        # Application styling
│   └── input-dynamic.js # Dynamic form handling
└── templates/
    ├── base.html         # Base HTML template
    ├── index.html        # Home/about page
    ├── about.html        # About page
    ├── input.html        # Manual input form
    ├── random_setup.html # Random setup form
    ├── random_input.html # Random input preview
    ├── result.html       # Results display
    └── error.html        # Error page
```

## Dependencies

- **Flask 2.3.2**: Web framework
- **fairpyx**: Fair division library with algorithm implementations
- **NumPy**: Numerical computing
- **gunicorn**: Production WSGI server
- **cffi**: C Foreign Function Interface

See `requirements.txt` for exact versions.

## References

- **Paper**: Markakis, E., & Psomas, C. A. (2011). *On Worst-Case Allocations in the Presence of Indivisible Goods*. WINE 2011.
  
## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Algorithms**: fairpyx library
- **Deployment**: gunicorn


## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Acknowledgments

This project implements the fair allocation algorithm described in the seminal work by Elias Markakis and Christos Psomas on worst-case analysis of indivisible goods allocation.
