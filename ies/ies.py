def ies(num_followers: int or list, num_likes: list, num_comments: list, mode='page'):
  """
  Parameters:

  1. num_followers: Total number of followers of a page, if mode is 'page'
                    List of number of followers of a page 24 hours after image was uploaded, if mode is 'image'
  2. num_likes: List of number of likes on each image on page (minimum length 10)
  3. num_comments: List of number of comments on each image on page (minimum length 10)
  4. mode: 'page' for p-IES, 'image' for i-IES

  Returns:

  ies: p-IES (float) or i-IES (list of floats)

  """

  assert len(num_likes) >= 10 and len(num_comments) >= 10, "Need data from at least 10 images"
  assert len(num_likes) == len(num_comments), "Mismatch in size of num_likes and num_comments"
  assert mode == 'page' or type(num_followers) == int, "i-IES expects list of number of followers"

  if mode == 'page':
    numerator = sum(num_likes) + sum(num_comments)
    denominator = num_followers
    ies = numerator/denominator
    print('The p-IES of the page is {:.2f}'.format(ies))

  elif mode == 'image':
    nums = [a+b for a, b in zip(num_likes, num_comments)]
    ies = [num/follower for num, follower in zip(nums, num_followers)]
    print('The i-IES of each image is ' + str(ies))

  else:
    print('Invalid mode selection. Please try again.')

  return ies

if __name__ == "__main__":

  ### EDIT ME! ###
  num_followers = 1
  num_likes = []
  num_comments = []
  mode = 'page'
  ################

  ies(num_followers, num_likes, num_comments, mode=mode)