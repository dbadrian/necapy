import json

from necapy import necapy


def train(model, dataset, model_params, cpu, e):
    print("training...")

def test():
    print("testing...")

def inference():
    print("inference...")

def random(model, dataset, model_params, cpu, e):
    print("called random")

if __name__ == "__main__":
    # create menu: base level (L0), a cmd-type
    menu = necapy(name='Hype', desc="Learning KG embeddings easily.")

    # L0 (main): 1st cmd (train)
    train_cmd = menu.add_command(name="train",
                                 desc="Train a model (new or continue from checkpoint",
                                 func=train)
    # L1 (train): add bunch of cmds
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
    test_cmd = menu.add_command("test", "Test a checkpoint model", func=test)

    # L0 (main): 3rd cmd
    inference_cmd = menu.add_command("inference", "Run inference on a dataset", func=inference)

    # L0 (main): 4th cmd
    list_cmd = menu.add_command("list", "List available models and datasets", func=None)
    list_models = list_cmd.add_command("models", "List available models", func=random)
    list_datasets = list_cmd.add_command("datasets", "List available datasets", func=random)
    list_datasets.add_argument('--model', '-m', type=str, default="ComplEx",
                           help="Name of model.")
    list_datasets.add_argument('--dataset', '-d', type=str, default="FB20K",
                           help="Name of dataset.")
    list_datasets.add_argument('--model_params', '-mp', type=json.loads,
                           default="{}",
                           help="Model parameters as dict (json-formatted)")
    list_datasets.add_argument('--cpu', action='store_true', help="Use CPU only.")
    list_datasets.add_argument('-e', type=int, default=1000,
                           help="Run for #e epochs.")

    menu.parse()
