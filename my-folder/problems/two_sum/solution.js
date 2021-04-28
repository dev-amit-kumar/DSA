var twoSum = function (nums, target) {
	var lookup = {};
	for (var i = 0; i < nums.length; i++) {
		let remainder = target - nums[i];
		if (remainder in lookup) {
			return [lookup[`${remainder}`], i];
		} else {
			lookup[nums[i]] = i;
		}
	}
};
