import BaseNavbar from "../components/BaseNavbar";

interface BaseLayoutProps {
  children: React.ReactNode;
}

const BaseLayout: React.FC<BaseLayoutProps> = ({ children }) => {
  return (
    <>
      <BaseNavbar />
      {children}
    </>
  );
};

export default BaseLayout;
