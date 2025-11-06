"""
Manages a simple inventory system.
Allows adding, removing and querying item quantities.
Supports loading/saving data to a JSON file.
"""
import json
# import logging
from datetime import datetime

# Global variable
# stock_data = {}


def add_item(stock_data, item="default", qty=0, logs=None):

    """
    Adds a specified quantity of an item to the stock.

    Args:
        stock_data (dict): The inventory dictionary to modify.
        item (str): The name of the item to add.
        qty (int): The quantity to add.
        logs (list, optional): A list to append log messages to.
    """

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(stock_data, item, qty):

    """
    Removes a specified quantity of an item from the stock.

    Args:
        stock_data (dict): The inventory dictionary to modify.
        item (str): The name of the item to remove.
        qty (int): The quantity to remove.
    """

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(stock_data, item):

    """
    Gets the current quantity of a specific item.

    Args:
        stock_data (dict): The inventory dictionary to query.
        item (str): The name of the item to query.

    Returns:
        int: The quantity of the item (0 if not found).
    """

    return stock_data[item]


def load_data(file="inventory.json"):

    """
    Loads inventory data from a JSON file.

    Args:
        file (str, optional): The name of the file to load.

    Returns:
        dict: The inventory data loaded from the file.
    """

    # f = open(file, "r")
    with open(file, 'r', encoding="UTF-8") as f:
        # global stock_data
        data = json.loads(f.read())
        f.close()
    return data


def save_data(stock_data, file="inventory.json"):

    """
    Saves the provided inventory data to a JSON file.

    Args:
        stock_data (dict): The inventory dictionary to save.
        file (str, optional): The name of the file to save to.
    """

    with open(file, 'w', encoding="UTF-8") as f:
        # f = open(file, "w")
        f.write(json.dumps(stock_data))
        f.close()


def print_data(stock_data):

    """
    Prints a formatted report of all items and their quantities.

    Args:
        stock_data (dict): The inventory dictionary to print.
    """

    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(stock_data, threshold=5):

    """
    Finds all items with a quantity below a specified threshold.

    Args:
        stock_data (dict): The inventory dictionary to check.
        threshold (int, optional): The stock level to check against.

    Returns:
        list: A list of item names that are low in stock.
    """

    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():

    """Main function to run the inventory management demo."""

    stock_data = {}
    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", -2)
    add_item(stock_data, 123, "ten")  # invalid types, no check
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)
    # eval("print('eval used')")  # dangerous


main()
