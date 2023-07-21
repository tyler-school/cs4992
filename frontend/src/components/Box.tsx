import React, { ReactNode } from 'react';


interface BoxProps {
  width: number | string;
  height: number | string;
  backgroundColor: string;
  children: ReactNode;
}

const Box: React.FC<BoxProps> = ({ width, height, backgroundColor, children }) => {
  const boxStyle: React.CSSProperties = {
    width,
    height,
    backgroundColor,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    border: '2px solid #000',
    boxShadow: '2px 2px 4px rgba(0, 0, 0, 0.2)',
    position: 'absolute',
    top: 0,
    right: 0,
  };

  
  return <div style={boxStyle}>{children}</div>;
};

export default Box;
