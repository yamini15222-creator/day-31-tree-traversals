import pytest

from assignment import (
    TreeNode,
    export_decision_tree,
    inorder,
    inorder_iterative,
    postorder,
    preorder,
    preorder_iterative,
)


def build_main_tree() -> TreeNode:
    

    return TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(4),
            right=TreeNode(5),
        ),
        right=TreeNode(3),
    )


def build_second_tree() -> TreeNode:
    

    return TreeNode(
        10,
        left=TreeNode(
            5,
            left=TreeNode(2),
            right=TreeNode(7),
        ),
        right=TreeNode(20),
    )


def build_skewed_tree() -> TreeNode:


    return TreeNode(
        1,
        right=TreeNode(
            2,
            right=TreeNode(
                3,
                right=TreeNode(4),
            ),
        ),
    )


def test_empty_tree() -> None:
    """Test recursive traversals with an empty tree."""

    assert preorder(None) == []
    assert inorder(None) == []
    assert postorder(None) == []


def test_empty_tree_iterative() -> None:
    """Test iterative traversals with an empty tree."""

    assert preorder_iterative(None) == []
    assert inorder_iterative(None) == []


def test_single_node() -> None:
    """Test all recursive traversals for a single-node tree."""

    single = TreeNode(10)

    assert preorder(single) == [10]
    assert inorder(single) == [10]
    assert postorder(single) == [10]


def test_single_node_iterative() -> None:
    """Test iterative traversals for a single-node tree."""

    single = TreeNode(10)

    assert preorder_iterative(single) == [10]
    assert inorder_iterative(single) == [10]


def test_main_tree() -> None:
    """Test recursive traversals using the main example tree."""

    root = build_main_tree()

    assert preorder(root) == [1, 2, 4, 5, 3]
    assert inorder(root) == [4, 2, 5, 1, 3]
    assert postorder(root) == [4, 5, 2, 3, 1]


def test_main_tree_iterative() -> None:
    """Test iterative traversals using the main example tree."""

    root = build_main_tree()

    assert preorder_iterative(root) == [1, 2, 4, 5, 3]
    assert inorder_iterative(root) == [4, 2, 5, 1, 3]


def test_second_tree() -> None:
    """Test recursive traversals using a second tree."""

    root = build_second_tree()

    assert preorder(root) == [10, 5, 2, 7, 20]
    assert inorder(root) == [2, 5, 7, 10, 20]
    assert postorder(root) == [2, 7, 5, 20, 10]


def test_second_tree_iterative() -> None:
    """Test iterative traversals using a second tree."""

    root = build_second_tree()

    assert preorder_iterative(root) == [10, 5, 2, 7, 20]
    assert inorder_iterative(root) == [2, 5, 7, 10, 20]


def test_skewed_tree() -> None:
    """Test recursive traversals using a skewed tree."""

    root = build_skewed_tree()

    assert preorder(root) == [1, 2, 3, 4]
    assert inorder(root) == [1, 2, 3, 4]
    assert postorder(root) == [4, 3, 2, 1]


def test_skewed_tree_iterative() -> None:
    """Test iterative traversals using a skewed tree."""

    root = build_skewed_tree()

    assert preorder_iterative(root) == [1, 2, 3, 4]
    assert inorder_iterative(root) == [1, 2, 3, 4]


def test_iterative_preorder_matches_recursive() -> None:
    """Verify iterative preorder matches recursive preorder."""

    root = build_main_tree()

    assert preorder(root) == preorder_iterative(root)


def test_iterative_inorder_matches_recursive() -> None:
    """Verify iterative inorder matches recursive inorder."""

    root = build_main_tree()

    assert inorder(root) == inorder_iterative(root)


def test_iterative_preorder_second_tree() -> None:
    """Compare iterative and recursive preorder on second tree."""

    root = build_second_tree()

    assert preorder(root) == preorder_iterative(root)


def test_iterative_inorder_second_tree() -> None:
    """Compare iterative and recursive inorder on second tree."""

    root = build_second_tree()

    assert inorder(root) == inorder_iterative(root)


def test_export_api() -> None:
    """Test the unified decision-tree export API."""

    root = build_main_tree()

    assert export_decision_tree(root, "preorder") == [
        1,
        2,
        4,
        5,
        3,
    ]

    assert export_decision_tree(root, "inorder") == [
        4,
        2,
        5,
        1,
        3,
    ]

    assert export_decision_tree(root, "postorder") == [
        4,
        5,
        2,
        3,
        1,
    ]


def test_invalid_order() -> None:
    """Test that an invalid traversal order raises ValueError."""

    root = build_main_tree()

    with pytest.raises(ValueError, match="Invalid traversal order"):
        export_decision_tree(root, "invalid")  # type: ignore[arg-type]


def test_tree_is_not_modified() -> None:
    """Verify that traversal does not modify the tree."""

    root = build_main_tree()

    original = preorder(root)

    export_decision_tree(root, "inorder")
    export_decision_tree(root, "postorder")

    assert preorder(root) == original