def distance_counter(d):
    """Counter of current distance

        Args:
          d: A positive number in string format.

        Returns:
          Value for future adding

        Raises:
          Exception: If input format is wrong.
        """
    try:
        d = float(d)
    except ValueError:
        raise Exception('Дистанция должна быть положительной')

    if d <= 0:
        raise Exception('Дистанция должна быть положительной')
    if d <= 2:
        return 50
    elif d <= 10:
        return 100
    elif d <= 30:
        return 200
    return 300


def size_counter(s):
    """Counter of current distance

        Args:
          s: A positive number in string format.

        Returns:
          Value for future adding

        Raises:
          Exception: If input format is wrong.
        """
    if s == '+':
        return 200
    elif s == '-':
        return 100
    else:
        raise Exception('Для габаритов груза используется \'+\' или \'-\'')


def careful_counter(c, l):
    """Counter of current distance

        Args:
            c: A positive number in string format.
            l: A character '+' or '-'

            Returns:
              Value for future adding

            Raises:
              Exception: If format value of value c is wrong or it is forbidden to sum up
            """
    l = float(l)
    if c == '+':
        if l > 30:
            raise Exception('Хрупкий груз нельзя далеко возить')
        return 300
    elif c == '-':
        return 0
    raise Exception('Для хрупкого груза используется \'+\' или \'-\'')


def koef_counter(k):
    """Counter of current distance

        Args:
          k: A non-negative integer number in string format from range [0, 3].

        Returns:
          Value for future adding

        Raises:
          Exception: If input format is wrong.
        """
    try:
        k = float(k)
    except ValueError:
        raise Exception('Коэффициент загрузки - целое число от 0 до 3')
    if k == 3:
        return 1.6
    elif k == 2:
        return 1.4
    elif k == 1:
        return 1.2
    elif k == 0:
        return 1
    else:
        raise Exception('Коэффициент загрузки - целое число от 0 до 3')


def counter(request):
    """Counter of current distance

        Args:
          request: A string of input parameters.

        Returns:
          Float result
        """
    try:
        length, size, careful, koef = request.split()
        res = (distance_counter(length) +
               size_counter(size) +
               careful_counter(careful, length)) * koef_counter(koef)
    except ValueError:
        return 'Дистанция, размеры и коэффициент должны быть неотрицательными числами, а хрупкость -\'+\' или \'-\''
    except Exception as e:
        return str(e)
    return res if res > 400 else 400


if __name__ == '__main__':
    print(counter(input()))
