import { IconType } from "react-icons";
import { AiOutlineHome } from "react-icons/ai";
import { BiSolidContact } from "react-icons/bi";
import StaticDir from "../utils/StaticDir";
import MultiLevelDropdown from "./MultiLevelDropdown";

const BaseNavbar = () => {
  interface navListType {
    name: string;
    url?: string;
    icon: IconType;
    children?: navListType[];
  }
  const navList: navListType[] = [
    {
      name: "home",
      url: "/",
      icon: AiOutlineHome,
    },
    {
      name: "contact",
      url: "/contact/",
      icon: BiSolidContact,
    },
  ];
  return (
    <nav className="bg-[#eeebe3] flex justify-between">
      <div className="p-4">
        <img src={StaticDir("logo.jpg")} className="h-12 rounded-full" />
      </div>
      <div className="p-4">
        <ul>
          <li></li>
        </ul>
      </div>
    </nav>
  );
};

export default BaseNavbar;
