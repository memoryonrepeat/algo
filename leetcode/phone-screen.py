Please use this Google doc during your interview (your interviewer will see what you write here). To free your hands for typing, we recommend using a headset or speakerphone.



Question:
---------
We would like to design an alerting system for a server.
The input to the system is error rates of the server over time.

Example:
  5, 10, 7, 15, 0, 60, 55, 60, 60, 60, 0, 5, 5, ...
  
means server having error rate of 
  5% during the 1st minute,
  10% during the 2nd minute,
  7% during the 3rd minute
and so on.

Alerts should go off if the system is unhealthy.

System is considered unhealthy at time T
 - if there is time interval [T0, T1]
   - lasts at least "minDuration" minutes
   - contains T
   - error rate is over "maxError" threshold for every minute of the interval.

Error rate > 5% for more that 15 minutes => unhealthy.
Was the system unhealthy yesterday at 5:30 PM? 

minDuration = T1 - T0 
lower bound (unhealthy period ends at T): (T - minDuration) -> T
upper bound (unhealthy period starts at T): T -> T + minDuration

T0 < T < T1

From T: as long as error rates > maxError, go to left, count how far
As soon as error rates <= maxError, stop, go to right, stop when duration > minDuration or error rate <= maxError (compare duration in this case).
duration = distance traveled so far
if duration > minDuration -> system unhealthy






def isUnhealthy(rates , T,  maxError):
	if rates[T] <= maxError:
		return False

	duration = 0
	current = T

	while rates[current] > maxError and current >= 0:
		current -= 1
		duration += 1
		if duration > minDuration:
			return True

	while rates[current] > maxError and current < len(rates):
		current += 1
		duration += 1
		if duration > minDuration:
			return True

	return (duration > minDuration)
	


positive test case
negative test case
edge cases - T is first / last index of the array
if T is first element of the array -> loop should stop when
if T is last element
if T is min element / max element

How to improve?

----------------------------------------

Now instead we want to tolerate small bursts.

System is considered unhealthy
 - if there is interval [T0, T1] where
   - interval contains T
   - min(error rate) * size > errorBudget








def isUnhealthy(rates , T,  maxError):

	duration = 1
	current = T
	min_rate = rates[T]

	while min_rate * duration <= maxError and current >= 0:
		current -= 1
		duration += 1
		min_rate = min(min_rate, rates[current])

	current = T+1

	while min_rate * duration <= maxError and current >= 0:
		current -= 1
		duration += 1
		min_rate = min(min_rate, rates[current])

	return False

------------------------------------------

