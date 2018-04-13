import json

from necapy import necapy


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
