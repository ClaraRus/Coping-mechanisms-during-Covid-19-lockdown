from dataset.Read_datasets import load_data


def extract_actions(text):
    actions = list()
    return actions


def main():
    path_dataset = 'C:\\Users\\Clara2\\Documents\\Radboud_Master\\Text and Multimedia Mining\\'
    dataset = load_data(path_dataset)
    for data in dataset:
        data.actions = extract_actions(data.text)


if __name__ == "__main__":
    main()
