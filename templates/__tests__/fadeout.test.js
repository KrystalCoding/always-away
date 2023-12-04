// Mocking jQuery fadeOut function
jest.mock('jquery', () => ({
  ...jest.requireActual('jquery'),
  fn: {
    fadeOut: jest.fn(),
  },
}));

// Import the fadeOutAlert function directly
import { fadeOutAlert } from '../../static/js/alerts';

// Test for fadeOutAlert function
test('fade out alert after 2 seconds', () => {
  // Mock setTimeout to immediately call the callback function
  jest.useFakeTimers();

  // Call the mocked fadeOutAlert function directly
  fadeOutAlert();

  // Fast-forward time by 2 seconds
  jest.advanceTimersByTime(2000);

  // Ensure that jQuery's fadeOut function is called
  expect($.fn.fadeOut).toHaveBeenCalledWith('slow');
});
