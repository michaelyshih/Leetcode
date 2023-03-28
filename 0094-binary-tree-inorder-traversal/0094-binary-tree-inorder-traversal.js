/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
function inorderTraversal(root) {
  let res = [];
  helper(root, res);
  return res;
}

function helper(root, res) {
  if (!root) {
    return res;
  }
  
  helper(root.left, res);
  res.push(root.val);
  helper(root.right, res);
  return res;
}