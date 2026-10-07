from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


TraversalOrder = Literal[
    "preorder",
    "inorder",
    "postorder",
]


@dataclass
class TreeNode:
    """Represent one node in a binary tree."""

    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def preorder(root: TreeNode | None) -> list[int]:
    """Return values using recursive preorder traversal."""

    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return

        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def inorder(root: TreeNode | None) -> list[int]:
    """Return values using recursive inorder traversal."""

    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return

        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result


def postorder(root: TreeNode | None) -> list[int]:
    """Return values using recursive postorder traversal."""

    result: list[int] = []

    def visit(node: TreeNode | None) -> None:
        if node is None:
            return

        visit(node.left)
        visit(node.right)
        result.append(node.value)

    visit(root)
    return result


def preorder_iterative(root: TreeNode | None) -> list[int]:
    """Return values using iterative preorder traversal.

    Order:
        Root -> Left -> Right
    """
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Right is pushed first because stack is LIFO.
        if node.right is not None:
            stack.append(node.right)

        # Left is pushed last so it is processed first.
        if node.left is not None:
            stack.append(node.left)

    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """Return values using iterative inorder traversal.

    Order:
        Left -> Root -> Right
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current is not None or stack:

        # Move to the leftmost node.
        while current is not None:
            stack.append(current)
            current = current.left

        # Process the node.
        current = stack.pop()
        result.append(current.value)

        # Process right subtree next.
        current = current.right

    return result


def _validate_order(order: str) -> None:
    """Validate traversal order."""

    valid_orders = {
        "preorder",
        "inorder",
        "postorder",
    }

    if order not in valid_orders:
        raise ValueError(
            f"Invalid traversal order: {order!r}. "
            f"Expected one of {sorted(valid_orders)}."
        )


def export_decision_tree(
    root: TreeNode | None,
    order: TraversalOrder,
) -> list[int]:
    """Export a decision tree using the requested traversal."""

    _validate_order(order)

    if order == "preorder":
        return preorder(root)

    if order == "inorder":
        return inorder(root)

    return postorder(root)