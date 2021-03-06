Notice: This is a project of mine to test some aspects of python, pypi, and others. Just use argparse/subparsers and for the most part, you will be fine! :)

# necapy
**NE**sted **C**ommand-line **A**rguments for **PY**thon is a tiny class allowing the quick creation of nested commandline-args/menu.

[THIS IS AN EARLY DRAFT. Description is not even close to correct/finished/updated yet]

It is powered by the standard library module *argparse* and adds the creation of nested submenus based on keywords.

You can add two types:
  * Command-submenu (followed by argparse menu, or other command-submenu)
  * Argparse-menu (leaf node)

## Example
An example says a thousand words -> Let's create a trivial example with 3 levels of hierarchy. 

Let's assume we are building a program to train some machine learning model, which has three modes: **train**, **test**, and **list**.
Train and test have no further subarguments, where list has two modes: **datasets** and **models**.

```python
import json

from necapy import necapy

# Some bogus functions which print their arguments
def train(model, dataset, model_params, cpu, e):
    print("function <train> called with:", locals())

def test():
    print("function <test> called with:", locals())

def list_d(dataset, model_params, cpu, e):
    print("function <list_d> called with:", locals())

def list_m(model, model_params):
    print("function <list_m> called with:", locals())

if __name__ == "__main__":
    # create menu: base level (L0), a cmd-type
    menu = necapy(name='Hype', desc="Learning KG embeddings easily.")

    # L0 (main): 1st cmd (train)
    train_cmd = menu.add_command(name="train",
                                 desc="Train a model (new or continue from checkpoint)",
                                 func=train)
    # L1 (train): add bunch of args
    train_cmd.add_argument('--model', '-m', type=str, default="ComplEx",
                           help="Name of model.")
    train_cmd.add_argument('--dataset', '-d', type=str, default="FB20K",
                           help="Name of dataset.")
    train_cmd.add_argument('--model_params', '-mp', type=json.loads,
                           default="{}",
                           help="Model parameters as dict (json-formatted)")
    train_cmd.add_argument('--cpu', action='store_true', help="Use CPU only.")
    train_cmd.add_argument('-e', type=int, default=1000,
                           help="Run for #e epochs.")

    # L0 (main): 2nd cmd
    test_cmd = menu.add_command("list", "List available models and datasets", func=None)

    # L0 (main): 3rd cmd
    list_cmd = menu.add_command("list", "List available models and datasets",
                                func=None)
    # L1 (list): add bunch of cmds
    list_models = list_cmd.add_command("models", "List available models",
                                       func=list_m)
    list_models.add_argument('--model', '-m', type=str, default="ComplEx",
                               help="Name of model.")
    list_models.add_argument('--model_params', '-mp', type=json.loads,
                               default="{}",
                               help="Model parameters as dict (json-formatted)")
    list_datasets = list_cmd.add_command("datasets", "List available datasets",
                                         func=list_d)

    # L2 (list_datasets): add bunch of cmds
    list_datasets.add_argument('--dataset', '-d', type=str, default="FB20K",
                               help="Name of dataset.")
    list_datasets.add_argument('--model_params', '-mp', type=json.loads,
                               default="{}",
                               help="Model parameters as dict (json-formatted)")
    list_datasets.add_argument('--cpu', action='store_true',
                               help="Use CPU only.")
    list_datasets.add_argument('-e', type=int, default=1000,
                               help="Run for #e epochs.")

    menu.parse()
```

lets make some calls:
```
dadrian@ullr ~/git/necapy ● python test.py

usage: Hype <command> [<args>]

Available commands:
   train          Train a model (new or continue from checkpoint
   test           Test a checkpoint model
   list           List available models and datasets
test.py: error: the following arguments are required: command
```

or

```
dadrian@ullr ~/git/necapy ● python test.py train -m "blub" --dataset "Nanana batman" -mp '{"cool_json":1337}' 

function train called with: {'e': 1000, 'cpu': False, 'model_params': {'cool_json': 1337}, 'dataset': 'Nanana batman', 'model': 'blub'}
```

or

```
dadrian@ullr ~/git/necapy ● python test.py list datasets -h 

usage: test.py [-h] [--model MODEL] [--dataset DATASET]
               [--model_params MODEL_PARAMS] [--cpu] [-e E]

List available datasets

optional arguments:
  -h, --help            show this help message and exit
  --model MODEL, -m MODEL
                        Name of model.
  --dataset DATASET, -d DATASET
                        Name of dataset.
  --model_params MODEL_PARAMS, -mp MODEL_PARAMS
                        Model parameters as dict (json-formatted)
  --cpu                 Use CPU only.
  -e E                  Run for #e epochs.

```

