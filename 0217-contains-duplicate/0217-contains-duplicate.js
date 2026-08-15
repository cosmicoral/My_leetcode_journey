/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const seen = new Set();
    for(let p =0; p<nums.length;p++){
        if(seen.has(nums[p])){
            return true;
        }
        seen.add(nums[p]);    
    }
    return false;
};