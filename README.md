This is a simple script that flips a whole website from rtl to ltr and vice versa.

It swaps every value for left and right margins and paddings, and replaces every "left" with "right" and vice versa.

Bear in mind that you need to assign a rtl direction and right text-align globally yourself, and this scirpt only swaps what's already in the css file.

**IMPORTANT: if any of your css class names include the phrae "right" or "left", they are also swapped, and you should update where you refer to them in your html file.**
