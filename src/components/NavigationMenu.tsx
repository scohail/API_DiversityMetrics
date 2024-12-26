import { Link } from "@tanstack/react-router";
import React from "react";

import ToggleTheme from "./ToggleTheme";

export default function NavigationMenu() {
    return (
        <nav>
            <ul className="flex flex-1 gap-2 p-2 text-sm items-center">
                <li>
                    <Link to="/">EDA</Link>
                </li>
                <li>
                    <Link to="/about">
                        Diversity
                    </Link>
                </li>
                <li className="ml-auto">
                    <ToggleTheme />
                </li>
            </ul>
        </nav>
    );
}
