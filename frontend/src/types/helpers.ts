// helpers.ts
import React from "react";

function moveLastToFront<T>(list: T[]): T[] {
    if (list.length > 1) {
        const lastElement = list.pop();
        if (lastElement !== undefined) {
            list.unshift(lastElement);
        }
    }

    return list;
}

export default moveLastToFront;