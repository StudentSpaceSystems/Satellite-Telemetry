// native-dependencies

#include <iostream>
#include <unistd.h>
#include <poll.h>
#include <sys/ioctl.h>
#include <string.h>

// non-native dependencies

int main (int argc, char * argv[])
{
	std::cout << "Arguments:" << std::endl;
	for (int i = 0; i < argc; i++)
	{
		std::cout << i << "\t";
		std::cout << argv[i] << std::endl;
	}

	struct pollfd fds[1];
	int timeout_msecs = -1;

	fds[0].fd = 0;
	fds[0].events = POLLHUP | POLLIN | POLLPRI;

	bool breakout_flag = false;
	char breakout_arr[] = { 'q','u','i','t', '\n', '\0' };
	char counter = 0;
	while (!breakout_flag)
	{
		std::cout << ">> " << "(" << (int) counter++ << ")" << std::endl;
		int ret = poll(fds, 1, timeout_msecs);
		if (ret > 0)
		{
			for (size_t i = 0; i < 1; i++)
			{
				if (fds[i].revents & POLLPRI || fds[i].revents & POLLIN)
				{
					int num_bytes = 0;
					int err = ioctl(fds[0].fd, FIONREAD, &num_bytes);
					char * byte_arr = (char *) malloc(num_bytes + 1);
					read(fds[i].fd, byte_arr, num_bytes);
					*(byte_arr + num_bytes + 1) = '\0';
					if (strcmp(byte_arr, breakout_arr) == 0)
					{
						breakout_flag = true;
						break;
					}
					std::cout << "You said (" << num_bytes << "): " << byte_arr << std::endl;
				}
				if (fds[i].revents & POLLHUP)
				{
				}
			}
		}
	}
	return 0;
}
