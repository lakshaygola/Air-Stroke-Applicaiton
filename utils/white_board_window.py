import cv2
import numpy as np


def create_color_box(board_canvas, box_x_position, box_y_position, box_color, box_text, box_text_position,
                     box_text_color):
    """
    Create and add color box on white board canvas
    :param board_canvas: white board object on which the color box needed to be created
    :param box_x_position: box position with resect of x-axis
    :param box_y_position: box position with resect of y-axis
    :param box_color: color of the box
    :param box_text: text of the box
    :param box_text_position: position of the text box
    :param box_text_color: color of the text of the box
    :return: return paint window object
    """
    cv2.rectangle(img=board_canvas, pt1=box_x_position, pt2=box_y_position, color=box_color, thickness=-1)
    cv2.putText(img=board_canvas, text=box_text, org=box_text_position, fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=0.6, color=box_text_color, thickness=1, lineType=cv2.LINE_AA)
    return board_canvas


def create_white_board_window():
    """
     Creates the paint window
    :return: return paint window object
    """
    canvas = np.ones((600, 736, 3))
    color_boxes = [
        {
            "box_color": (200, 200, 200),
            "x_position": (35, 5),
            "y_position": (130, 65),
            "box_text": "CLEAR",
            "box_text_position": (50, 38),
            "font_color": (0, 0, 0)
        },
        {
            "box_color": (255, 0, 0),
            "x_position": (155, 5),
            "y_position": (245, 65),
            "box_text": "BLUE",
            "box_text_position": (175, 38),
            "font_color": (0, 0, 0)
        },
        {
            "box_color": (0, 255, 0),
            "x_position": (265, 5),
            "y_position": (360, 65),
            "box_text": "GREEN",
            "box_text_position": (288, 38),
            "font_color": (0, 0, 0)
        },
        {
            "box_color": (0, 0, 255),
            "x_position": (380, 5),
            "y_position": (475, 65),
            "box_text": "RED",
            "box_text_position": (410, 38),
            "font_color": (0, 0, 0)
        },
        {
            "box_color": (0, 255, 255),
            "x_position": (495, 5),
            "y_position": (590, 65),
            "box_text": "YELLOW",
            "box_text_position": (510, 38),
            "font_color": (0, 0, 0)
        },
    ]

    for color_box in color_boxes:
        canvas = create_color_box(board_canvas=canvas, box_x_position=color_box.get("x_position"),
                                  box_y_position=color_box.get("y_position"),
                                  box_color=color_box.get("box_color"),
                                  box_text=color_box.get("box_text"),
                                  box_text_position=color_box.get("box_text_position"),
                                  box_text_color=color_box.get("font_color"))
    cv2.namedWindow('White Board', cv2.WINDOW_AUTOSIZE)
    return canvas


if __name__ == '__main__':
    canvas = create_white_board_window()
    while True:
        cv2.imshow('White Board', canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()