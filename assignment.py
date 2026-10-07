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


def _validate_order(order: str) -> None:
    """Validate the requested traversal order."""

    valid_orders = {"preorder", "inorder", "postorder"}

    if order not in valid_orders:
        raise ValueError(
            f"Invalid traversal order: {order!r}. "
            f"Expected one of {sorted(valid_orders)}."
        )


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
    """Return values using iterative preorder traversal."""

    if root is None:
        return []

    result: list[int] = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Stack is LIFO, so right must be pushed first.
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """Return values using iterative inorder traversal."""

    result: list[int] = []
    stack: list[TreeNode] = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)

        current = current.right

    return result


def export_decision_tree(
    root: TreeNode | None,
    order: TraversalOrder,
) -> list[int]:
    """
    Export a decision tree according to the requested traversal order.

    Args:
        root: Root node of the binary decision tree.
        order: preorder, inorder, or postorder.

    Returns:
        Node values in the requested traversal order.

    Raises:
        ValueError: If the traversal order is invalid.
    """

    _validate_order(order)

    if order == "preorder":
        return preorder(root)

    if order == "inorder":
        return inorder(root)

    return postorder(root)